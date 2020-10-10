let mocha = require('mocha');
let chai = require('chai');
let it = mocha.it;
var yeetUtil = require('../util/yeet')

it("yeet yeet yeet", function() {
    let result = yeetUtil.yeet()
    chai.assert(result != null);
    console.log(`Result: ${result}`);
    chai.assert(result === "yeet", "The result of yeetUtil.yeet should be yeet")
});
