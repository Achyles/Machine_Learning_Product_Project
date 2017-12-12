import $ from 'jquery'
import './index.css'


// Some page elements
const $inputField = $('#input');
const $expandButton = $('#expand');
const $responseField = $('#responseField');

// AJAX functions

function expandUrl() {
    const urlToExpand = 'http://localhost:7777/review/?review=' + $inputField.val();

    const result =$.ajax({
        url: urlToExpand,
        type: 'GET',
        success(response) {
            console.log(response);
            $responseField.append('<p>' + response + '</p>');
        }, error(jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });
}

function expan() {
    $responseField.empty();
    expandUrl();
    return false;
}

// Call functions on submit

$expandButton.click(expan);
