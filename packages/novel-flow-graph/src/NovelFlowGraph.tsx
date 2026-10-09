import {
  EditorRenderer,
  FreeLayoutEditorProvider,
  type FreeLayoutPluginContext,
  type FreeLayoutProps,
  useNodeRender,
  usePlaygroundTools,
  type WorkflowJSON,
  type WorkflowNodeProps,
  WorkflowNodeRenderer,
} from '@flowgram.ai/free-layout-editor';
import {
  createMinimapPlugin,
  MinimapRender,
} from '@flowgram.ai/minimap-plugin';
import {
  Crosshair,
  GitBranch,
  Minus,
  PanelRightClose,
  Plus,
  Search,
  Sparkles,
} from 'lucide-react';
import { useMemo, useRef, useState } from 'react';

import type {
  GraphView,
  NovelFlowGraphProps,
  NovelGraphNodeData,
} from './types';
import './styles.css';
import '@flowgram.ai/free-layout-editor/index.css';

const VIEW_LABELS: Record<GraphView, string> = {
  spine: '主干',
  entities: '实体',
  chapters: '章节',
  all: '全量',
};

const KIND_LABELS: Record<string, string> = {
  root: '小说',
  category: '分类',
  character: '人物',
  event: '事件',
  faction: '势力',
  location: '地点',
  term: '术语',
  object: '物件',
  chapter: '章节',
  scene: '场景',
  plot: '剧情',
  system: '规则',
  other: '其他',
};

function StoryNode({
  node,
  onOpen,
}: WorkflowNodeProps & { onOpen: (data: NovelGraphNodeData) => void }) {
  const { selected } = useNodeRender(node);
  const data = node.getJSONData() as NovelGraphNodeData;
  return (
    <WorkflowNodeRenderer
      className={`nfg-node nfg-node--${data.kind}${selected ? ' is-selected' : ''}`}
      node={node}
    >
      <button
        className="nfg-node__body"
        type="button"
        onClick={() => onOpen(data)}
      >
        <span className="nfg-node__kind">
          {KIND_LABELS[data.kind] ?? data.kind}
        </span>
        <strong>{data.title}</strong>
        {data.summary && (
          <span className="nfg-node__summary">{data.summary}</span>
        )}
      </button>
    </WorkflowNodeRenderer>
  );
}

function CanvasTools() {
  const tools = usePlaygroundTools({ minZoom: 0.05, maxZoom: 2 });
  return (
    <div className="nfg-tools">
      <button type="button" title="放大" onClick={() => tools.zoomin()}>
        <Plus size={16} />
      </button>
      <span>{Math.round(tools.zoom * 100)}%</span>
      <button type="button" title="缩小" onClick={() => tools.zoomout()}>
        <Minus size={16} />
      </button>
      <button
        type="button"
        title="适应画布"
        onClick={() => tools.fitView(true)}
      >
        <Crosshair size={16} />
      </button>
      <button
        type="button"
        title="自动布局"
        onClick={() => void tools.autoLayout()}
      >
        <Sparkles size={16} />
      </button>
    </div>
  );
}

function matchesView(node: WorkflowJSON['nodes'][number], view: GraphView) {
  const data = node.data as NovelGraphNodeData;
  if (view === 'all') return true;
  if (view === 'entities') return data.kind !== 'chapter';
  if (view === 'chapters')
    return ['root', 'category', 'chapter'].includes(data.kind);
  if (['root', 'category', 'event', 'plot'].includes(data.kind)) return true;
  return (
    data.kind === 'chapter' && Boolean(data.chapter && data.chapter % 25 === 0)
  );
}

function filterGraph(
  data: NovelFlowGraphProps['data'],
  view: GraphView,
  query: string,
): WorkflowJSON {
  const normalized = query.trim().toLocaleLowerCase();
  const visible = new Set(
    data.nodes
      .filter((item) => {
        const nodeData = item.data as NovelGraphNodeData;
        if (!matchesView(item, view)) return false;
        if (!normalized) return true;
        return `${nodeData.title} ${nodeData.summary} ${nodeData.sourcePath}`
          .toLocaleLowerCase()
          .includes(normalized);
      })
      .map((item) => item.id),
  );
  if (normalized) {
    for (const item of data.nodes) {
      const nodeData = item.data as NovelGraphNodeData;
      if (nodeData.kind === 'root' || nodeData.kind === 'category')
        visible.add(item.id);
    }
  }
  const nodes = data.nodes.filter((item) => visible.has(item.id));
  const roots = nodes.filter(
    (item) => (item.data as NovelGraphNodeData).kind === 'root',
  );
  const categories = nodes.filter(
    (item) => (item.data as NovelGraphNodeData).kind === 'category',
  );
  const content = nodes.filter(
    (item) =>
      !['root', 'category'].includes((item.data as NovelGraphNodeData).kind),
  );
  const columns = view === 'spine' ? 7 : view === 'entities' ? 12 : 24;
  const positioned = [
    ...roots.map((item, index) => ({
      ...item,
      meta: { ...item.meta, position: { x: index * 260, y: 0 } },
    })),
    ...categories.map((item, index) => ({
      ...item,
      meta: {
        ...item.meta,
        position: {
          x: (index - (categories.length - 1) / 2) * 260,
          y: 210,
        },
      },
    })),
    ...content.map((item, index) => ({
      ...item,
      meta: {
        ...item.meta,
        position: {
          x: (index % columns) * 260 - ((columns - 1) * 260) / 2,
          y: 460 + Math.floor(index / columns) * 130,
        },
      },
    })),
  ];
  return {
    nodes: positioned,
    edges: data.edges.filter(
      (item) =>
        visible.has(item.sourceNodeID) && visible.has(item.targetNodeID),
    ),
  };
}

export function NovelFlowGraph({
  data,
  initialView = 'spine',
  onNodeOpen,
}: NovelFlowGraphProps) {
  const [view, setView] = useState<GraphView>(initialView);
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState<NovelGraphNodeData | null>(null);
  const contextRef = useRef<FreeLayoutPluginContext>(null);
  const graph = useMemo(
    () => filterGraph(data, view, query),
    [data, query, view],
  );
  const editorProps = useMemo<FreeLayoutProps>(
    () => ({
      background: true,
      readonly: true,
      initialData: graph,
      enableReadonlyNodeDragging: true,
      nodeRegistries: [
        {
          type: 'novel-node',
          meta: {
            defaultPorts: [{ type: 'input' }, { type: 'output' }],
          },
        },
      ],
      getNodeDefaultRegistry: (type) => ({ type, meta: {} }),
      materials: {
        renderDefaultNode: (props: WorkflowNodeProps) => (
          <StoryNode
            {...props}
            onOpen={(nodeData) => {
              setSelected(nodeData);
              onNodeOpen?.(nodeData);
            }}
          />
        ),
      },
      plugins: () => [
        createMinimapPlugin({
          disableLayer: true,
          canvasStyle: {
            canvasWidth: 184,
            canvasHeight: 104,
            canvasPadding: 14,
            canvasBackground: '#ffffff',
            viewportBackground: 'rgba(30, 111, 92, 0.08)',
            viewportBorderColor: '#1e6f5c',
            nodeColor: '#667085',
          },
        }),
      ],
      onAllLayersRendered: (context) => {
        window.setTimeout(() => context.tools.fitView(false), 0);
      },
    }),
    [graph, onNodeOpen],
  );

  const coverage = data.coverage;
  return (
    <section className="nfg-shell">
      <header className="nfg-header">
        <div className="nfg-title">
          <GitBranch size={18} />
          <div>
            <h1>{data.novel.title}</h1>
            <p>
              {coverage.nodes} 节点 · {coverage.edges} 关系 ·{' '}
              {coverage.chapters} 章 · {coverage.rewrittenChapters} 重构 ·{' '}
              {coverage.orphanNodes} 孤点
            </p>
          </div>
        </div>
        <div className="nfg-search">
          <Search size={15} />
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="搜索人物、事件、章节"
            aria-label="搜索图谱"
          />
        </div>
        <nav className="nfg-segments" aria-label="图谱视图">
          {(Object.keys(VIEW_LABELS) as GraphView[]).map((item) => (
            <button
              className={view === item ? 'is-active' : ''}
              type="button"
              key={item}
              onClick={() => setView(item)}
            >
              {VIEW_LABELS[item]}
            </button>
          ))}
        </nav>
      </header>
      <div className="nfg-stage">
        <FreeLayoutEditorProvider
          key={`${view}:${query}`}
          ref={contextRef}
          {...editorProps}
        >
          <EditorRenderer className="nfg-canvas" />
          <CanvasTools />
          <div className="nfg-minimap">
            <MinimapRender
              containerStyles={{
                position: 'relative',
                inset: 'auto',
                pointerEvents: 'auto',
              }}
              inactiveStyle={{
                opacity: 1,
                scale: 1,
                translateX: 0,
                translateY: 0,
              }}
            />
          </div>
        </FreeLayoutEditorProvider>
        <aside className={`nfg-detail${selected ? ' is-open' : ''}`}>
          {selected && (
            <>
              <button
                className="nfg-detail__close"
                type="button"
                title="关闭详情"
                onClick={() => setSelected(null)}
              >
                <PanelRightClose size={17} />
              </button>
              <span className={`nfg-badge nfg-badge--${selected.kind}`}>
                {KIND_LABELS[selected.kind] ?? selected.kind}
              </span>
              <h2>{selected.title}</h2>
              <p>{selected.summary || '暂无摘要。'}</p>
              <dl>
                <dt>状态</dt>
                <dd>{selected.status}</dd>
                <dt>可信度</dt>
                <dd>{selected.canon}</dd>
                {selected.chapter && (
                  <>
                    <dt>章号</dt>
                    <dd>{selected.chapter}</dd>
                  </>
                )}
                <dt>来源</dt>
                <dd>{selected.sourcePath}</dd>
              </dl>
            </>
          )}
        </aside>
      </div>
    </section>
  );
}
