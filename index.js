//import { dump } from "js-yaml";

import { elements } from "./elements.js";

function spaces(text) {    
    for(let i = 0; i < text.length; i++)
        if(text[i] != ' ')
            return parseInt((i+2)/4);
    return 0;
}

// *****************************************************************************************************
// process1
// Get string and return list of lines and spaces
function process1(layout) {
    const lines = layout.split('\n');
    const list = [];
    for(const rawline of lines) {
        //const line = rawline.split('#')[0];
        const line = rawline;
        if(line.trim() == '') continue;
        const space = spaces(line);
        const attributes = line.trim().split(' ');
        const name = attributes[0];
        let props = null;
        if(attributes.length > 1)
            props = attributes.slice(-attributes.length+1);
        list.push({space,name,props,children:[]});
    }
    return list;
}

// *****************************************************************************************************
// process2
// Get list of lines and return tree
function process2(list) {
    const root = {space: -1, name:'dialog', parent:null, children: []};
    let last_node = root;
    for(const node of list) {
        if(node.space == last_node.space) {
            last_node.parent.children.push(node);
            node.parent = last_node.parent;
        }
        else if(node.space > last_node.space) {
            last_node.children.push(node);
            node.parent = last_node;
        } else {
            let parent = last_node;
            while(parent.space >= node.space) {
                parent = parent.parent;
            }
            node.parent = parent;
            parent.children.push(node);
        }
        last_node = node;
    }
    return root;
}

// *****************************************************************************************************
// process3
// Get tree and return html
function process3(tree) {
    let html = "";
    let classes ="";
    let innerHTML = "";
    if(tree.name) {
        if(elements.hasOwnProperty(tree.name)) {
            const element = elements[tree.name];
            html+= element.start_tag.slice(0,-1);
            classes = element.classes;
        } else {
            html+= `<${tree.name}`;
        }
        
        if(tree.props) {
            for(const prop of tree.props) {
                const [key,value] = prop.split('=');
                if(value) {
                    if(key == 'class')
                        classes += " " + value.replace(/\+/g, ' ');
                    else
                        html+= ` ${key}="${value}"`;
                }
                else {
                    if(key.startsWith('m'))
                        classes += ` ${key}`;
                    else
                        innerHTML += `${key.replace(/_/g," ")}`;
                }
            }
        }
        if(classes)
            html+= ` class="${classes}"`;
        html+= ">" + innerHTML;
    }    
    for(const child of tree.children) {
        html+= process3(child);
    }
    if(tree.name) {
        if(elements.hasOwnProperty(tree.name)) {
            const element = elements[tree.name];
            html+= element.end_tag;
        } else {
            html+= `</${tree.name}>`;
        }
    }
    return html;
}

function parse(layout) {
    let list = process1(layout);

    let tree = process2(list);

    let html = process3(tree);

    return html;
}

export class dialog {
    init(layout,appid) {
        this.layout = layout;
        this.appid = appid;
        this.render(appid);
    }
    test() {
        console.log("test");
    }
    render(elementId) {
        let app_element = document.getElementById(elementId);
        const html = parse(this.layout);
        if(app_element) {
            app_element.innerHTML = html;
        } else {
            console.log(`app element ${elementId} not found`);
        }
    }    
}


export { parse };
