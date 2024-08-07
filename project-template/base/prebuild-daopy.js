// You may need to update this file if something changes in the future.
const fs=require("fs");
const path=require("path");
let config={};
config=JSON.parse(fs.readFileSync("./dao3.config.json",{encoding:"utf-8"}));
function buildDaopyServer(){
    let serverPath=path.dirname(path.join(config.ArenaPro.file.typescript.server.base,config.ArenaPro.file.typescript.server.entry));
    let daopyServerPath=path.join(serverPath,"daopy-server");
    let project=toProject(daopyServerPath);
    // generateCode
    let code=`import {defaultProjectRunner} from 'daopy-npm';
defaultProjectRunner(${JSON.stringify(project)});`;
    fs.writeFileSync(path.join(serverPath,"_daopy_bundle.ts"),code);
}
function buildDaopyClient(){
    let clientPath=path.dirname(path.join(config.ArenaPro.file.typescript.client.base,config.ArenaPro.file.typescript.client.entry));
    let daopyClientPath=path.join(clientPath,"daopy-client");
    let project=toProject(daopyClientPath);
    // generateCode
    let code=`import {defaultProjectRunner} from 'daopy-npm/client';
defaultProjectRunner(${JSON.stringify(project)});`;
    fs.writeFileSync(path.join(clientPath,"_daopy_bundle.ts"),code);
}
function toProject(folder){
    let project={mods:{},entry:"index"};
    fs.readdirSync(folder,{recursive:true}).forEach((file)=>{
        file=file.replaceAll("\\","/");
        if(path.dirname(file)=="dao3"||file=="dao3")return;
        // is file
        if(!fs.statSync(path.join(folder,file)).isDirectory())project.mods[`./${file}`]=fs.readFileSync(path.join(folder,file)).toString();
    });
    return project;
}
console.log("building server")
buildDaopyServer();
console.log("building client");
buildDaopyClient();
console.log("[prebuilt success]")// do not change this line
console.log("预构建已完成")