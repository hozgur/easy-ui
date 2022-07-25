const {tokenizeElement} = require('./easy-ui.js');

let sampleLine = 'row  .w8 .center class=" testValue " .{ testClass } { testText } ';
test("tokenize Element Test", () => {
    expect(tokenizeElement(sampleLine)).toEqual([
        "row",
        ".w8",
        ".center",
        'class=" testValue "',
        ".{ testClass }",
        "{ testText }"
    ]);
});

