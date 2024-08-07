// The module 'vscode' contains the VS Code extensibility API

// import { spawn.sync } from 'node:child_process';

// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
const util = require('node:util');
const execFile = util.promisify(require('child_process').execFile);
const spawn = require('cross-spawn');
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
async function chooseWorkspace() {
	let folders = vscode.workspace.workspaceFolders;
	if (!folders) {
		vscode.window.showErrorMessage("未检测到已打开的工作区");
		return;
	}
	let folder = folders[0];
	if (folders.length > 1) {
		folder = await vscode.window.showWorkspaceFolderPick({ placeHolder: "请选择要创建项目的文件夹" });
		if (!folder) return;
	}
	return folder;
}
async function prebuild() {
	let folder = await chooseWorkspace();
	if (!folder) return;
	vscode.window.showInformationMessage("预构建运行中...");
	let res = spawn.sync("npm", ["run", "prebuild"], { cwd: folder.uri.fsPath });
	console.log(res)
	if (res.stdout.toString().includes("[prebuilt success]")) {
		vscode.window.showInformationMessage("预构建成功");
		return true;
	} else {
		vscode.window.showErrorMessage(`预构建失败${res.stderr.toString()}`);
		return false;
	}
}
let implementTplUrls = {
	"micropython": "/project-template/mpy",
	"esbuild-js": "/project-template/esbuild-js",
}
let nobaseTpls = ["esbuild-js"]
function activate(context) {
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Arena Pro Ext Daopy is active.');
	context.subscriptions.push(vscode.commands.registerCommand('arena-pro-ext-daopy.create-project', async () => {
		let folder = await chooseWorkspace();
		if (!folder) return;
		// check if folder empty
		let files = await vscode.workspace.fs.readDirectory(folder.uri);
		if (files.length > 0) { vscode.window.showErrorMessage("文件夹不为空，请选择一个空文件夹来创建项目"); return; }
		// choose implement
		let implements_select = [
			"[Python3] Skulpt.js(纯js实现) [!推荐!]",
			"[Python3](beta) MicroPython(Wasm实现[速度缓慢;Server端;存在bug见插件介绍;Client端会继续使用Skulpt.js])",
			"[JavaScript](beta) Esbuild打包js后嵌入arenapro(ts) 但是为什么不去学TypeScript呢？"
		]
		let implement = await vscode.window.showQuickPick(implements_select, { placeHolder: "请选择解释器：", canPickMany: false });
		if (!implement) return;
		// implement=implement[0];
		if (Array.isArray(implement)) implement = implement[0];
		if (implement == implements_select[0]) implement = "skulpt";
		else if (implement == implements_select[1]) implement = "micropython";
		else if (implement == implements_select[2]) implement = "esbuild-js";
		else {
			vscode.window.showErrorMessage(`未知的解释器类型 ${implement}`);
			return;
		}
		console.log(`implement selected: ${implement}`);
		vscode.window.showInformationMessage("正在复制ap-dpy模板……");

		if (!nobaseTpls.includes(implement)) {
			// copy ext/project-template/base to folder
			let tplPathUri = context.extensionUri;
			tplPathUri = tplPathUri.with({ path: tplPathUri.path + "/project-template/base" });
			let copyfiles = await vscode.workspace.fs.readDirectory(tplPathUri);

			for (let file of copyfiles) {
				if (file[0].includes("node_modules")) continue;
				if (file[0].includes("package-lock.json")) continue;
				await vscode.workspace.fs.copy(tplPathUri.with({ path: tplPathUri.path + "/" + file[0] }), folder.uri.with({ path: folder.uri.path + "/" + file[0] }), { overwrite: true });
			}
		}
		// implement-specific files
		if (implement != "skulpt") {
			let implementTplUrl = context.extensionUri;
			implementTplUrl = implementTplUrl.with({ path: implementTplUrl.path + implementTplUrls[implement] });
			let implementFiles = await vscode.workspace.fs.readDirectory(implementTplUrl);
			for (let file of implementFiles) {
				await vscode.workspace.fs.copy(implementTplUrl.with({ path: implementTplUrl.path + "/" + file[0] }), folder.uri.with({ path: folder.uri.path + "/" + file[0] }), { overwrite: true });
			}
		}

		vscode.window.showInformationMessage("正在运行项目初始化...等待终端运行结束即可");
		let term = await vscode.window.createTerminal({ name: "ap-dpy: init", cwd: folder.uri });
		term.show(false);
		term.sendText("npm install --registry=https://mirrors.huaweicloud.com/repository/npm/");
		term.sendText("npm run check-daopy");
	}));
	context.subscriptions.push(vscode.commands.registerCommand('arena-pro-ext-daopy.prebuild-project', async () => {
		await prebuild();
	}))
	context.subscriptions.push(vscode.commands.registerCommand('arena-pro-ext-daopy.deploy-project', async () => {
		let pre_stat = await prebuild();
		if (!pre_stat) return;
		await vscode.commands.executeCommand("ap.file.buildNUpload");
	}))
}

// This method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
