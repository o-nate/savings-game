// In-page elements
let explain = document.getElementById('explain');
let confirmation = document.getElementById('confirm');
let no_cost = document.getElementById('no_cost');
let yes_cost = document.getElementById('yes_cost');
let explanation_text = document.getElementById('explanation_text');

// Variables from python
let response = js_vars.response;
let options = js_vars.answer_options;
let explanations = js_vars.explanations;
let costType = js_vars.cost_type;

function select_explanation(cost) {
    // Determine if negation should be included in follow-up question
    add_no = function (response_options) {
        if (response_options[2] === 'true') {
            no_cost.classList.remove('do-not-show');
            // Remove affirmative from follow-up question
            yes_cost.classList.add('do-not-show');
        }
    }
    // Display explanation
    let response_option = options[response];
    add_no(options);
    explanation_text.innerText = explanations[response][response_option];

}

select_explanation(costType);