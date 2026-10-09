import { defineConfig } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';

export default defineConfig({
  plugins: [pluginReact()],
  html: {
    title: '小说闭环图谱',
  },
  output: {
    distPath: {
      root: '../../dist/story-graph',
    },
  },
});
