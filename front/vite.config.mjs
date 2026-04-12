import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';
import autoprefixer from 'autoprefixer';
import { execSync } from 'child_process'; // Добавляем импорт

export default defineConfig(() => {
    return {
        base: '/static/',
        build: {
            outDir: '../back/data/static/',
            rollupOptions: {
                plugins: [
                    {
                        name: 'build-start-plugin',
                        buildStart() {
                            console.log('📦 Rollup starting...');
                            execSync('rm -rf ../back/data/static/*');
                        },
                        buildEnd() {
                            console.log('📦 Rollup completed successfully');
                        },
                    },
                ],
            },
        },
        css: {
            postcss: {
                plugins: [
                    autoprefixer({}), // add options if needed
                ],
            },
        },
        esbuild: {
            loader: 'jsx',
            include: /src\/.*\.jsx?$/,
            exclude: [],
        },
        optimizeDeps: {
            force: true,
            esbuildOptions: {
                loader: {
                    '.js': 'jsx',
                },
            },
        },
        plugins: [
            react(),
            {
                name: 'execute-shell-post-build',
                closeBundle() {
                    const nf = '../back/money_app/src/templates/index.html';
                    const rf = '../back/data/static/index.html';
                    console.log('📦 Bundle post-build copy files...');
                    execSync(`rm -rf ${nf}`);
                    execSync(`cp ${rf} ${nf}`);
                    console.log('📦 Bundle post-build completed successfully');
                },
            },
        ],
        resolve: {
            alias: [
                {
                    find: 'src/',
                    replacement: `${path.resolve(__dirname, 'src')}/`,
                },
            ],
            extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.scss'],
        },
        server: {
            port: 3000,
        },
    };
});
