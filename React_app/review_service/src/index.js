// Include data for accessing Google APIs
import $ from 'jquery'
import './index.css'

const apiKey = 'AIzaSyCrg82Taj3Rm_96Idv-EXg7zq12bHmJEig';
const url = 'https://www.googleapis.com/urlshortener/v1/url';

// Some page elements

const $inputField = $('#input');
const $expandButton = $('#expand');
const $shortenButton = $('#shorten');
const $responseField = $('#responseField');

// AJAX functions

function expandUrl() {
    const urlToExpand = 'http://localhost:7777/review/?review=' + $inputField.val();
    //const urlToExpand = 'http://localhost:7777/rank/?rank=COMS+W4111+W1004+W4995';
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

    /*const con = 1;
    $.ajax({
        url: 'http://localhost:7777/chart2',
        data: JSON.stringify({'courseNumber':'W4111 W1004 W4995'}),
        contentType: 'application/x-www-form-urlencoded',
        type: 'POST',
        success: function(response) {
            //console.log(response);
            console.log(con);
        },
        error: function(error) {
            console.log(error);
        }
    });*/


    /*const result = fetch(urlToExpand, {
        method: 'POST',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({"test_1": "1"})
    }).then(response => {
        if (response.ok) {
        return response.json();
    }
    throw new Error('Request failed!');
}, networkError => console.log(networkError.message)).then(jsonResponse => {
        $responseField.append('<p> Your shortened URL is </p><p>' + jsonResponse.id + '</p>');
    return jsonResponse;
});
    console.log(result);*/
}

function shortenUrl() {
    const urlWithKey = url + '?key=' + apiKey;
    const urlToShorten = $inputField.val();

    $.ajax({
        url: urlWithKey,
        type: 'POST',
        data: JSON.stringify({longUrl: urlToShorten}),
        dataType: 'json',
        contentType: 'application/json',
        success(response) {
            $responseField.append('<p>Your shortened url is: </p><p>' + response.id + '</p>');
        },
        error(jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });
}

function expan() {
    $responseField.empty();
    expandUrl();
    return false;
}

function shorten() {
    $responseField.empty();
    shortenUrl();
    return false;
}

// Call functions on submit

$expandButton.click(expan);
$shortenButton.click(shorten);
