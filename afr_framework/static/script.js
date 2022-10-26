const graph = document.getElementById("graph_type");
const columns = document.forms["form_checkbox"].getElementsByTagName("input");
var graph1Dic = {
  bar: 0,
  line: 0,
  pie: 0,
  scatter: 0,
};
var graph2Dic = {
  bar: 0,
  line: 0,
  pie: 0,
  scatter: 0,
};
var graph3Dic = {
  bar: 0,
  line: 0,
  pie: 0,
  scatter: 0,
};
var graph4Dic = {
  bar: 0,
  line: 0,
  pie: 0,
  scatter: 0,
};
var graph5Dic = {
  bar: 0,
  line: 0,
  pie: 0,
  scatter: 0,
};
const graphDicArray = [graph1Dic, graph2Dic, graph3Dic, graph4Dic, graph5Dic];
var count = 0;

function printGraphArray() {
  for (var i of graphDicArray) {
    console.log(i);
  }
}

function graphNumberSelectValidation() {
  const graphNumber = document.getElementById("select_graph");
  const graphOptions = graph.getElementsByTagName("options");
  var graphSelected = document.querySelectorAll('[selected="selected"]');
  const graphOptionsId = document.querySelectorAll('[name="option1"]');
  const graphNumberId = document.querySelectorAll('[name="option0"]');

  console.log(event.currentTarget);

  for (var i = 0; i < graphNumberId.length; i++) {
    graphNumberId[i].removeAttribute("selected");
  }

  for (var i = 0; i < graphOptionsId.length; i++) {
    graphOptionsId[i].removeAttribute("selected");
  }

  for (var i = 0; i < columns.length; i++) {
    if (columns[i].checked === true) {
      columns[i].checked === false;
    } else console.log("Already Unchecked");
  }

  for (var i = 0; i < graphNumberId.length; i++) {
    if (event.currentTarget.value === graphNumberId[i].getAttribute("value")) {
      graphNumberId[i].setAttribute("selected", "selected");
      graphSelected = document.querySelectorAll('[selected="selected"]');
    } else console.log(`Not ${i}`);
  }
}

function graphCheckboxValidation() {
  var graphSelected = document.querySelectorAll('[selected="selected"]');
  count = 0;
  for (var i = 0; i < columns.length; i++) {
    if (columns[i].type === "checkbox" && columns[i].checked === true) {
      count++;
    }
  }
  console.log(count);
  if (count === 2) {
    for (var i = 0; i < columns.length; i++) {
      if (!columns[i].checked === true) {
        columns[i].disabled = true;
        console.log(`Disabled Column`);
      }
    }
  }
  if (count === 1) {
    for (var i = 0; i < columns.length; i++) {
      if (columns[i].checked === false) {
        columns[i].disabled = false;
        console.log(`Enabled Column`);
      }
    }
  }
  for (var i = 0; i < columns.length; i++) {
    if (columns[i].checked === true) {
      if (graphSelected[0].getAttribute("value") === "1") {
        graph1Dic[i] = "checked";
        printGraphArray();
      }
    } else {
      if (columns[i].checked === false) {
        if (graphSelected[0].getAttribute("value") === "1") {
          delete graph1Dic[i];
        }
      }
    }
    if (columns[i].checked === true) {
      if (graphSelected[0].getAttribute("value") === "2") {
        graph2Dic[i] = "checked";
        printGraphArray();
      }
    } else {
      if (columns[i].checked === false) {
        if (graphSelected[0].getAttribute("value") === "2") {
          delete graph2Dic[i];
        }
      }
    }
    if (columns[i].checked === true) {
      if (graphSelected[0].getAttribute("value") === "3") {
        graph3Dic[i] = "checked";
        printGraphArray();
      }
    } else {
      if (columns[i].checked === false) {
        if (graphSelected[0].getAttribute("value") === "3") {
          delete graph3Dic[i];
        }
      }
    }
    if (columns[i].checked === true) {
      if (graphSelected[0].getAttribute("value") === "4") {
        graph4Dic[i] = "checked";
        printGraphArray();
      }
    } else {
      if (columns[i].checked === false) {
        if (graphSelected[0].getAttribute("value") === "4") {
          delete graph4Dic[i];
        }
      }
    }
    if (columns[i].checked === true) {
      if (graphSelected[0].getAttribute("value") === "5") {
        graph5Dic[i] = "checked";
        printGraphArray();
      }
    } else {
      if (columns[i].checked === false) {
        if (graphSelected[0].getAttribute("value") === "5") {
          delete graph5Dic[i];
        }
      }
    }
  }

  // for (var i = 0; i < columns.length; i++) {
  //     if (columns[i].checked === false) {
  //         if (graphSelected[0].getAttribute("value") === "1") {
  //             var key = Object.keys(graph1Dic)
  //             if (key[i] === columns[i]) {
  //                 graph1Dic.splice(i)
  //             }
  //         }
  //     }
  // }
}

function graphTypeSelect() {
  const graphNumber = document.getElementById("select_graph");
  const graphOptions = graph.getElementsByTagName("options");
  var graphSelected = document.querySelectorAll('[selected="selected"]');
  const graphOptionsId = document.querySelectorAll('[name="option1"]');

  for (var i = 0; i < graphOptionsId.length; i++) {
    graphOptionsId[i].removeAttribute("selected");
  }

  for (var i = 0; i < graphOptionsId.length; i++) {
    if (event.currentTarget.value === graphOptionsId[i].getAttribute("value")) {
      graphOptionsId[i].setAttribute("selected", "selected");
      graphSelected = document.querySelectorAll('[selected="selected"]');
    } else console.log(`Error ${i}`);
  }

  console.log(graphSelected[0].getAttribute("name"));
  console.log(graphSelected[1].getAttribute("name"));

  console.log(event.currentTarget);
  if (graphSelected[0].getAttribute("value") === "1") {
    if (graphSelected[1].getAttribute("value") === "1") {
      graph1Dic["bar"] = 1;
      return printGraphArray();
    } else {
      graph1Dic["bar"] = 0;
    }
    if (graphSelected[1].getAttribute("value") === "2") {
      graph1Dic["line"] = 1;
      return printGraphArray();
    } else {
      graph1Dic["line"] = 0;
    }
    if (graphSelected[1].getAttribute("value") === "3") {
      graph1Dic["pie"] = 1;
      return printGraphArray();
    } else {
      graph1Dic["pie"] = 0;
    }
    if (graphSelected[1].getAttribute("value") === "4") {
      graph1Dic["scatter"] = 1;
      return printGraphArray();
    } else {
      graph1Dic["scatter"] = 0;
    }
  } else {
    if (graphSelected[0].getAttribute("value") === "2") {
      if (graphSelected[1].getAttribute("value") === "1") {
        graph2Dic["bar"] = 1;
        return printGraphArray();
      } else {
        graph2Dic["bar"] = 0;
      }
      if (graphSelected[1].getAttribute("value") === "2") {
        graph2Dic["line"] = 1;
        return printGraphArray();
      } else {
        graph2Dic["line"] = 0;
      }
      if (graphSelected[1].getAttribute("value") === "3") {
        graph2Dic["pie"] = 1;
        return printGraphArray();
      } else {
        graph2Dic["pie"] = 0;
      }
      if (graphSelected[1].getAttribute("value") === "4") {
        graph2Dic["scatter"] = 1;
        return printGraphArray();
      } else {
        graph2Dic["scatter"] = 0;
      }
    } else {
      if (graphSelected[0].getAttribute("value") === "3") {
        if (graphSelected[1].getAttribute("value") === "1") {
          graph3Dic["bar"] = 1;
          return printGraphArray();
        } else {
          graph3Dic["bar"] = 0;
        }
        if (graphSelected[1].getAttribute("value") === "2") {
          graph3Dic["line"] = 1;
          return printGraphArray();
        } else {
          graph3Dic["line"] = 0;
        }
        if (graphSelected[1].getAttribute("value") === "3") {
          graph3Dic["pie"] = 1;
          return printGraphArray();
        } else {
          graph3Dic["pie"] = 0;
        }
        if (graphSelected[1].getAttribute("value") === "4") {
          graph3Dic["scatter"] = 1;
          return printGraphArray();
        } else {
          graph3Dic["scatter"] = 0;
        }
      } else {
        if (graphSelected[0].getAttribute("value") === "4") {
          if (graphSelected[1].getAttribute("value") === "1") {
            graph4Dic["bar"] = 1;
            return printGraphArray();
          } else {
            graph4Dic["bar"] = 0;
          }
          if (graphSelected[1].getAttribute("value") === "2") {
            graph4Dic["line"] = 1;
            return printGraphArray();
          } else {
            graph4Dic["line"] = 0;
          }
          if (graphSelected[1].getAttribute("value") === "3") {
            graph4Dic["pie"] = 1;
            return printGraphArray();
          } else {
            graph4Dic["pie"] = 0;
          }
          if (graphSelected[1].getAttribute("value") === "4") {
            graph4Dic["scatter"] = 1;
            return printGraphArray();
          } else {
            graph4Dic["scatter"] = 0;
          }
        } else {
          if (graphSelected[0].getAttribute("value") === "5") {
            if (graphSelected[1].getAttribute("value") === "1") {
              graph5Dic["bar"] = 1;
              return printGraphArray();
            } else {
              graph5Dic["bar"] = 0;
            }
            if (graphSelected[1].getAttribute("value") === "2") {
              graph5Dic["line"] = 1;
              return printGraphArray();
            } else {
              graph5Dic["line"] = 0;
            }
            if (graphSelected[1].getAttribute("value") === "3") {
              graph5Dic["pie"] = 1;
              return printGraphArray();
            } else {
              graph5Dic["pie"] = 0;
            }
            if (graphSelected[1].getAttribute("value") === "4") {
              graph5Dic["scatter"] = 1;
              return printGraphArray();
            } else {
              graph5Dic["scatter"] = 0;
            }
          }
        }
      }
    }
  }
}

const column_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];

let txt = "";
for (let x in column_names) {
  txt +=
    "<input id=' name=' type='checkbox' onclick='graphCheckboxValidation()'>" +
    column_names[x] +
    "<br>";
}

document.getElementById("form_checkbox").innerHTML = txt;
