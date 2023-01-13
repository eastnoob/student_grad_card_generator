// const command = 'markdown.marp.export';
// const command = 'workbench.action.openRawDefaultSettings';

// vscode.commands.executeCommand(command);

vscode.commands.executeCommand('workbench.action.openRawDefaultSettings').then(result => {
    console.log(result);
});