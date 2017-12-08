// Include data for accessing Google APIs
import $ from 'jquery'

const apiKey = '';
const url = 'https://www.googleapis.com/urlshortener/v1/url';

// Some page elements

const $inputField = $('#input');
const $expandButton = $('#expand');
const $shortenButton = $('#shorten');
const $responseField = $('#responseField');

// AJAX functions

function expandUrl() {
    /*const urlToExpand = url +
        '?key=' + apiKey +
        '&shortUrl=' + $inputField.val();*/
    const urlToExpand = 'http://localhost:7777/chart2';
    /*const result =$.ajax({
        url: urlToExpand,
        type: 'GET',
        dataType: 'json',
        success(response) {
            $responseField.append('<p>Your expanded url is: </p><p>' + response.longUrl + '</p>');
        }, error(jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });*/
    /*const result = $.ajax({
        url: 'http://localhost:7777/chart2',
        contentType: "application/json; charset=utf-8",
        crossDomain: true,
        data: JSON.stringify({"test_1":"1","test_2":"2"}),
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
    console.log(result);*/
    const result = fetch(urlToExpand, {
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
    console.log(result);
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
