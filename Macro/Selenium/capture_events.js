(function() {
    let actions = [];

    // Captura cliques
    document.addEventListener('click', function(event) {
        let path = event.composedPath();
        let element = path[0];
        let selector = element.tagName.toLowerCase();

        // Cria seletor básico
        if (element.id) {
            selector += `#${element.id}`;
        } else if (element.className) {
            selector += `.${element.className.split(' ').join('.')}`;
        }

        actions.push({
            type: 'click',
            selector: selector,
            timestamp: Date.now()
        });
    });

    // Captura entradas de texto
    document.addEventListener('input', function(event) {
        let path = event.composedPath();
        let element = path[0];
        let selector = element.tagName.toLowerCase();

        if (element.id) {
            selector += `#${element.id}`;
        } else if (element.className) {
            selector += `.${element.className.split(' ').join('.')}`;
        }

        actions.push({
            type: 'input',
            selector: selector,
            value: element.value,
            timestamp: Date.now()
        });
    });

    // Exibe log quando ESC é pressionado
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            console.log('Ações registradas:', JSON.stringify(actions));
        }
    });
})();
