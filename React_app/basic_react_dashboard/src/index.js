// Include data for accessing Google APIs
import $ from 'jquery'
import './index.css'

const apiKey = 'AIzaSyCrg82Taj3Rm_96Idv-EXg7zq12bHmJEig';
const url = 'https://www.googleapis.com/urlshortener/v1/url';

// Some page elements

const $inputField = $('#input');
const $rankButton = $('#but1');
const $recButton = $('#but2');
const $reviewButton = $('#but3');
const $shortenButton = $('#shorten');
const $responseField = $('#responseField');

// AJAX functions

function rankUrl() {
    const urlOfRank = 'http://localhost:7777/rank/?rank=' + $inputField.val();
    //const urlToExpand = 'http://localhost:7777/rank/?rank=COMS+W4111+W1004+W4995';
    const result =$.ajax({
        url: urlOfRank,
        type: 'GET',
        success(response) {
            console.log(response);
            $responseField.append('<p>The rank of courses is: </p><p>' + response + '</p>');
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

function recUrl() {
    const urlOfRec = 'http://localhost:7777/rec/?rec=' + $inputField.val();
    //const urlToExpand = 'http://localhost:7777/rank/?rank=COMS+W4111+W1004+W4995';
    const result =$.ajax({
        url: urlOfRec,
        type: 'GET',
        success(response) {
            console.log(response);
            $responseField.append('<p>The recommended courses are: </p><p>' + response + '</p>');
        }, error(jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });
}

function reviewUrl() {
    const urlOfRev = 'http://localhost:7777/review/?review=' + $inputField.val();
    //const urlToExpand = 'http://localhost:7777/rank/?rank=COMS+W4111+W1004+W4995';
    const result =$.ajax({
        url: urlOfRev,
        type: 'GET',
        success(response) {
            console.log(response);
            $responseField.append('<p>The review of courses are: </p><p>' + response + '</p>');
        }, error(jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });
}

function rank() {
    $responseField.empty();
    rankUrl();
    return false;
}

function recommend() {
    $responseField.empty();
    recUrl();
    return false;
}

function review() {
    $responseField.empty();
    reviewUrl();
    return false;
}

// Call functions on submit

$rankButton.click(rank);
$recButton.click(recommend);
$reviewButton.click(review);