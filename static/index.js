function hideShow() {
    e = document.getElementById("container")
    if (e.style.display === "none") {
        e.style.display = "block";
        document.getElementById("d").innerHTML = "(hide settings)"
    } else {
        e.style.display = "none";
        document.getElementById("d").innerHTML = "(show settings)"
    }
}
function work(s) {

    $.ajax({
        type: 'POST',
        url: '/',
        data: { "q": s, "t": "integral", "upper": document.getElementById("upper").value, "lower": document.getElementById("lower").value, "blocks": document.getElementById("n_val").value },
        success: function (response) {
            document.getElementById("integral").innerHTML = response
        },
        error: function (error) {
            console.error('POST request failed.');
            console.error('Error:', error);
        }
    });
    $.ajax({
        type: 'POST',
        url: '/',
        data: { "q": s, "t": "midpoint", "upper": document.getElementById("upper").value, "lower": document.getElementById("lower").value, "blocks": document.getElementById("n_val").value },
        success: function (response) {
            document.getElementById("midpoint").innerHTML = response
        },
        error: function (error) {
            console.error('POST request failed.');
            console.error('Error:', error);
        }
    });
    $.ajax({
        type: 'POST',
        url: '/',
        data: { "q": s, "t": "left", "upper": document.getElementById("upper").value, "lower": document.getElementById("lower").value, "blocks": document.getElementById("n_val").value },
        success: function (response) {
            document.getElementById("left").innerHTML = response
        },
        error: function (error) {
            console.error('POST request failed.');
            console.error('Error:', error);
        }
    });
    $.ajax({
        type: 'POST',
        url: '/',
        data: { "q": s, "t": "right", "upper": document.getElementById("upper").value, "lower": document.getElementById("lower").value, "blocks": document.getElementById("n_val").value },
        success: function (response) {
            document.getElementById("right").innerHTML = response
        },
        error: function (error) {
            console.error('POST request failed.');
            console.error('Error:', error);
        }
    });
}

function update(s) {
    if (s == "1") {
        math = '\\int_{' + document.getElementById("lower").value + '}^{' + document.getElementById("upper").value + '} \\sin(x) \\, dx'
        document.getElementById("latex_code").src = 'https://math.vercel.app/?from=' + math
    } else if (s == "2") {
        math = '\\int_{' + document.getElementById("lower").value + '}^{' + document.getElementById("upper").value + '} \\cos(x) \\, dx'
        document.getElementById("latex_code").src = 'https://math.vercel.app/?from=' + math
    } else if (s == "3") {
        math = '\\int_{' + document.getElementById("lower").value + '}^{' + document.getElementById("upper").value + '} \(x^2) \\, dx'
        document.getElementById("latex_code").src = 'https://math.vercel.app/?from=' + math
    }
}


$(document).ready(function () {
    work($('#items').val())
    document.getElementById("n_val").oninput = function () {
        document.getElementById("n_count").innerHTML = '"n" value: ' + this.value;
        update($('#items').val())
        work($('#items').val())
    };
    document.getElementById("upper").oninput = function () {
        document.getElementById("uc").innerHTML = 'Upper bound value: ' + this.value;
        update($('#items').val())
        work($('#items').val())
    };
    document.getElementById("lower").oninput = function () {
        document.getElementById("lc").innerHTML = 'Lower bound value: ' + this.value;
        update($('#items').val())
        work($('#items').val())
    };
    $('#items').change(function () {
        var s = $(this).val();
        update(s)
        work(s)
    });
});