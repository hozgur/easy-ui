
import {easyUI} from './easy-ui.js';

const app = new easyUI();

window.app = app;

const layout = `
row
    panel .p4
        h3 .p4 { Hello_World }
    panel .p4
        row .w8 .center
            h3 from_Easy-UI
        row .right .w8
            button Test_Button onclick=app.test_button()
            

`;

app.test_button = function() {
    alert('Test Button');
};

window.onload = function() {
    app.init(layout,"myapp");
}