const path = require('path');
let HtmlWebpackPlugin = require('html-webpack-plugin');
let HtmlWebpackInlineSourcePlugin = require('html-webpack-inline-source-plugin');

module.exports = {
    publicPath: '',
    outputDir: path.resolve(__dirname, 'vue_boilerplate', 'output', 'dist'),
    filenameHashing: false,
    pages: {
        index: {
            // entry for the page
            entry: 'vue_boilerplate/output/src/main.js',
            // the source template
            template: 'vue_boilerplate/output/public/index.html',
            // output as dist/index.html
            filename: 'index.html',
            chunks: ['chunk-vendors', 'index']
        },
    },
    css: {extract: false},

    chainWebpack: config => {
        if (process.env.NODE_ENV === 'development') {
            config.plugins
                .delete('preload')
                .delete('prefetch');
        }
        config
            .plugin('html-webpack-inline-source-plugin')
            .use(HtmlWebpackInlineSourcePlugin)
        config
            .plugin('html-webpack-plugin')
                .use(new HtmlWebpackPlugin({
                    inlineSource: '.(js|css)$', // embed all javascript and css inline
                    inject: true,
                    template: 'vue_boilerplate/output/public/index.html',  //template file to embed the source
                    title: 'Cloudsplaining report',
                }
            ));
        config.optimization
            .splitChunks({
                name: false,
                chunks: 'async',
                hidePathInfo: true,
            });
        config.module
            .rule('md')
                .test(/\.md$/)
                .use('html-loader')
                .loader("html-loader")
                .end()
                .use('markdown-loader')
                .loader("markdown-loader")
    }
}
