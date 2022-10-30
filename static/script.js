const formInput = document.getElementById("graphColumnSelect");
const formInputs = formInput.getElementsByTagName("input");
var formGraphArray = new Array();
var countArray = new Array()


if (document.body.contains(document.getElementById("graphInfo1_p2"))) {
    const graph1 = document.getElementById("graphInfo1_p2");
    const graph1Input = graph1.querySelectorAll("input");
    var count1 = 0;
    var formInputArray1 = new Array();
    for (var i = 0; i < graph1Input.length; i++) { formInputArray1.push(graph1Input[i]) }
    formGraphArray.push(graph1);
    countArray.push(count1);
}
if (document.body.contains(document.getElementById("graphInfo2_p2"))) {
    const graph2 = document.getElementById("graphInfo2_p2");
    const graph2Input = graph2.querySelectorAll("input");
    var count2 = 0;
    var formInputArray2 = new Array();
    for (var i = 0; i < graph2Input.length; i++) { formInputArray2.push(graph2Input[i]) }
    formGraphArray.push(graph2);
    countArray.push(count2);
}
if (document.body.contains(document.getElementById("graphInfo3_p2"))) {
    const graph3 = document.getElementById("graphInfo3_p2");
    const graph3Input = graph3.querySelectorAll("input");
    var count3 = 0;
    var formInputArray3 = new Array();
    for (var i = 0; i < graph3Input.length; i++) { formInputArray3.push(graph3Input[i]) }
    formGraphArray.push(graph3);
    countArray.push(count3);
}
if (document.body.contains(document.getElementById("graphInfo4_p2"))) {
    const graph4 = document.getElementById("graphInfo4_p2");
    const graph4Input = graph4.querySelectorAll("input");
    var count4 = 0;
    var formInputArray4 = new Array();
    for (var i = 0; i < graph4Input.length; i++) { formInputArray4.push(graph4Input[i]) }
    formGraphArray.push(graph4);
    countArray.push(count4);
}
if (document.body.contains(document.getElementById("graphInfo5_p2"))) {
    const graph5 = document.getElementById("graphInfo5_p2");
    const graph5Input = graph5.querySelectorAll("input");
    var count5 = 0;
    var formInputArray5 = new Array();
    for (var i = 0; i < graph5Input.length; i++) { formInputArray5.push(graph5Input[i]) }
    formGraphArray.push(graph5);
    countArray.push(count5);
}

function graphCheckboxValidation() {
    for (var i = 0; i < countArray.length; i++) {
        countArray[i] = 0;
    }
    for (let i in formInputArray1) {
        if (formInputArray1[i].checked === true) {
            countArray[0]++;
        }
    }
    for (let i in formInputArray2) {
        if (formInputArray2[i].checked === true) {
            countArray[1]++;
        }
    }
    for (let i in formInputArray3) {
        if (formInputArray3[i].checked === true) {
            countArray[2]++;
        }
    }
    for (let i in formInputArray4) {
        if (formInputArray4[i].checked === true) {
            countArray[3]++;
        }
    }
    for (let i in formInputArray5) {
        if (formInputArray5[i].checked === true) {
            countArray[4]++;
        }
    }

    if (countArray[0] === 2) {
        for (var i = 0; i < formInputArray1.length; i++) {
            if (formInputArray1[i].checked === false) {
                formInputArray1[i].disabled = true;
            }
        }
    }
    if (countArray[1] === 2) {
        for (var i = 0; i < formInputArray2.length; i++) {
            if (formInputArray2[i].checked === false) {
                formInputArray2[i].disabled = true;
            }
        }
    }
    if (countArray[2] === 2) {
        for (var i = 0; i < formInputArray3.length; i++) {
            if (formInputArray3[i].checked === false) {
                formInputArray3[i].disabled = true;
            }
        }
    }
    if (countArray[3] === 2) {
        for (var i = 0; i < formInputArray4.length; i++) {
            if (formInputArray4[i].checked === false) {
                formInputArray4[i].disabled = true;
            }
        }
    }
    if (countArray[4] === 2) {
        for (var i = 0; i < formInputArray5.length; i++) {
            if (formInputArray5[i].checked === false) {
                formInputArray5[i].disabled = true;
            }
        }
    }

    if (countArray[0] === 0 || countArray[0] === 1) {
        for (var i = 0; i < formInputArray1.length; i++) {
            if (formInputArray1[i].checked === false) {
                formInputArray1[i].disabled = false;
            }
        }
    }
    if (countArray[1] === 0 || countArray[1] === 1) {
        for (var i = 0; i < formInputArray2.length; i++) {
            if (formInputArray2[i].checked === false) {
                formInputArray2[i].disabled = false;
            }
        }
    }
    if (countArray[2] === 0 || countArray[2] === 1) {
        for (var i = 0; i < formInputArray3.length; i++) {
            if (formInputArray3[i].checked === false) {
                formInputArray3[i].disabled = false;
            }
        }
    }
    if (countArray[3] === 0 || countArray[3] === 1) {
        for (var i = 0; i < formInputArray4.length; i++) {
            if (formInputArray4[i].checked === false) {
                formInputArray4[i].disabled = false;
            }
        }
    }
    if (countArray[4] === 0 || countArray[4] === 1) {
        for (var i = 0; i < formInputArray5.length; i++) {
            if (formInputArray5[i].checked === false) {
                formInputArray5[i].disabled = false;
            }
        }
    }

}