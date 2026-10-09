import type { WorkflowJSON } from '@flowgram.ai/free-layout-editor';

export type GraphView = 'spine' | 'entities' | 'chapters' | 'all';

export type NovelNodeKind =
  | 'root'
  | 'category'
  | 'character'
  | 'event'
  | 'faction'
  | 'location'
  | 'term'
  | 'object'
  | 'chapter'
  | 'scene'
  | 'plot'
  | 'system'
  | 'other';

export interface NovelGraphNodeData {
  title: string;
  kind: NovelNodeKind;
  summary: string;
  canon: string;
  status: string;
  sourcePath: string;
  chapter?: number;
  phase?: string;
  aliases?: string[];
  evidenceCount?: number;
  completeness?: number;
}

export interface NovelGraphEdgeData {
  relation: string;
  weight?: number;
}

export interface NovelGraphDataset {
  schemaVersion: number;
  novel: {
    id: string;
    title: string;
    generatedAt: string;
  };
  coverage: {
    wikiPages: number;
    indexedPages: number;
    chapters: number;
    rewrittenChapters: number;
    linkedChapters: number;
    nodes: number;
    edges: number;
    orphanNodes: number;
  };
  nodes: NonNullable<WorkflowJSON['nodes']>;
  edges: NonNullable<WorkflowJSON['edges']>;
}

export interface NovelFlowGraphProps {
  data: NovelGraphDataset;
  initialView?: GraphView;
  onNodeOpen?: (node: NovelGraphNodeData) => void;
}
