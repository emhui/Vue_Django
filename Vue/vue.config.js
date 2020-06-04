// vue.config.js
module.exports = {
    css: {
        loaderOptions: {
            less: {
                modifyVars: {
/*                     'primary-color': '#ff0000',
                    'link-color': '#1DA57A',
                    'border-radius-base': '200px', */
                     'primary-color': 'rgba(42,42,42,0.7)',
                    'component-background' : 'rgba(42,42,42,0.7)',
                    'border-color-base': '#444',
                    'text-color': '#fff',
                    'background-color-light': 'rgba(42, 42, 42, 0.7)',
                    'heading-color': '#fff'
                },
                javascriptEnabled: true,
            },
        },
    },
};
