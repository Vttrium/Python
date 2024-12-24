(function () {
    let actions = [];

    function createSelector(element) {
        let selector = element.tagName.toLowerCase();
        if (element.id) {
            selector += `#${element.id}`;
        } else if (element.className) {
            selector += `.${element.className.split(' ').join('.')}`;
        }
    
        // Validação de unicidade
        if (document.querySelectorAll(selector).length > 1) {
            selector = getXPath(element);  // Fallback para XPath
        }
    
        return selector;
    }
    
    function getXPath(element) {
        let path = [];
        while (element && element.nodeType === Node.ELEMENT_NODE) {
            let index = Array.prototype.indexOf.call(
                element.parentNode.children,
                element
            ) + 1;
            path.unshift(`${element.tagName}[${index}]`);
            element = element.parentNode;
        }
        return path.length ? "/" + path.join("/") : null;
    }    

    // Captura cliques
    document.addEventListener('click', function (event) {
        let element = event.target;
        let selector = createSelector(element);

        actions.push({
            type: 'click',
            selector: selector,
            timestamp: Date.now()
        });

        // Salva no localStorage
        localStorage.setItem('actions', JSON.stringify(actions));
    });

    // Captura entradas de texto
    document.addEventListener('input', function (event) {
        let element = event.target;
        let selector = createSelector(element);

        actions.push({
            type: 'input',
            selector: selector,
            value: element.value,
            timestamp: Date.now()
        });

        // Salva no localStorage
        localStorage.setItem('actions', JSON.stringify(actions));
    });

    // Captura mudanças em campos de seleção
    document.addEventListener('change', function (event) {
        let element = event.target;
        let selector = createSelector(element);

        actions.push({
            type: 'change',
            selector: selector,
            value: element.value,
            timestamp: Date.now()
        });

        // Salva no localStorage
        localStorage.setItem('actions', JSON.stringify(actions));
    });

    // Exibe log quando ESC é pressionado
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            console.log('Ações registradas:', JSON.stringify(actions));
        }
    });

    // Carrega ações previamente salvas
    window.addEventListener('load', function () {
        const savedActions = localStorage.getItem('actions');
        if (savedActions) {
            actions = JSON.parse(savedActions);
            console.log('Ações carregadas:', actions);
        }
    });
})();
