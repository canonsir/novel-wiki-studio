import { NovelFlowGraph, type NovelGraphDataset } from '@novel-wiki/flow-graph';
import { AlertTriangle, LoaderCircle } from 'lucide-react';
import { useEffect, useState } from 'react';

interface Manifest {
  novels: Array<{
    id: string;
    title: string;
    file: string;
  }>;
}

type LoadState =
  | { status: 'loading' }
  | { status: 'error'; message: string }
  | { status: 'ready'; data: NovelGraphDataset };

export function App() {
  const [state, setState] = useState<LoadState>({ status: 'loading' });

  useEffect(() => {
    const load = async () => {
      const manifestResponse = await fetch('/data/manifest.json');
      if (!manifestResponse.ok) throw new Error('无法读取小说图谱清单');
      const manifest = (await manifestResponse.json()) as Manifest;
      const requested = new URLSearchParams(window.location.search).get(
        'novel',
      );
      const target =
        manifest.novels.find((item) => item.id === requested) ??
        manifest.novels[0];
      if (!target) throw new Error('还没有可用的小说图谱');
      const graphResponse = await fetch(`/data/${target.file}`);
      if (!graphResponse.ok) throw new Error(`无法读取图谱：${target.title}`);
      setState({
        status: 'ready',
        data: (await graphResponse.json()) as NovelGraphDataset,
      });
    };
    void load().catch((error: unknown) => {
      setState({
        status: 'error',
        message: error instanceof Error ? error.message : '图谱加载失败',
      });
    });
  }, []);

  if (state.status === 'loading') {
    return (
      <main className="app-state">
        <LoaderCircle className="app-spin" size={24} />
        <span>正在装载小说知识图谱</span>
      </main>
    );
  }
  if (state.status === 'error') {
    return (
      <main className="app-state app-state--error">
        <AlertTriangle size={24} />
        <span>{state.message}</span>
      </main>
    );
  }
  return <NovelFlowGraph data={state.data} />;
}
