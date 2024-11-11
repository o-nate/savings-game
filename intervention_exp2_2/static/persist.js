function persistInput(inp) {
    let isCheckbox = inp.type === 'checkbox';
    /*  checkboxes work differently from other form inputs.
        The 'checked' attribute stores whether it's checked or not.
        'valueInput' should generally be hardcoded to 1.
     */
    let valueAttr = isCheckbox ? 'checked' : 'value';
    let key = `input-${pageNumber}-${inp.name}`;
    let storedValue = sessionStorage.getItem(key);
    if (storedValue != null) {
        // with radios, you have multiple inputs that all have the same name.
        // this is how to check the right one.
        form[inp.name][valueAttr] = storedValue;
    }

    inp.addEventListener('input', function () {
        let curValue = inp[valueAttr];
        // needed because sessionStorage implicitly converts true/false to strings
        if (isCheckbox) curValue = curValue ? 'checked' : '';
        console.log('typeof Input:', key, curValue);
        sessionStorage.setItem(key, curValue);
    });
}

function persistClass(pageElement, className) {
    let key = `${pageNumber}-${pageElement.id}`;
    let classString = className;
    if (className === null) classString = classString ? className.toString() : '';
    console.log('persist', pageElement, key, classString);
    sessionStorage.setItem(key, classString);

}

// since sessionStorage persists across pages,
// we don't want to contaminate other pages in the same session
// whose fields happen to have the same name.
let urlParts = window.location.pathname.split('/');
let lastIndex = urlParts.length - 1
let pageNumber = urlParts[lastIndex];
// in case the path somehow has a trailing slash
if (pageNumber === '') pageNumber = urlParts[lastIndex - 1];
let form;
costID = `id_q_${costType}-`
// console.log(costType, costID);

document.addEventListener("DOMContentLoaded", function (event) {
    form = document.getElementById('form');
    for (let inp of document.querySelectorAll(`[id^=id_q_${costType}-]`)) {
        console.log(inp);
        persistInput(inp);
    }
    for (state of current_classes) {
        let stateObject = document.getElementById(state)
        persistClass(stateObject, stateObject.getAttribute('class'));
    }
    for (let inp of document.querySelectorAll(`[id^=id_confirm_${costType}-]`)) {
        console.log(inp);
        persistInput(inp);
    }
});