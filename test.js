
import {dialog} from './index.js';

const app = new dialog();

window.app = app;

const layout = `
row
    panel c_p4
        h3 Hello_World
    panel c_p4
        row c_w8 c_center
            h3 from_Easy-UI
        row c_right c_w8
            button Test_Button onclick=app.test_button()
            

`;

app.test_button = function() {
    alert('Test Button');
};

window.onload = function() {
    app.init(layout,"myapp");
}