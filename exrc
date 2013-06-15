function! SyncToPi()
    let resp = system('./sync.sh')
endfunction
autocmd BufWritePost * call SyncToPi()
