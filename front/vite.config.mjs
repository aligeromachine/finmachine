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
                name: 'execute-shell-script',
                closeBundle() {
                    try {
                        console.log('Running post-build script...');
                        execSync('./copy_script.sh');
                        console.log('Post-build script completed successfully');
                    } catch (error) {
                        console.error('Error executing post-build script:', error);
                        process.exit(1);
                    }
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
