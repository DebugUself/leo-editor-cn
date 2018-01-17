# Leo 中文文档翻译计划

## Notice 
This is not [the official leo repository](https://github.com/leo-editor/leo-editor). We've been working on translating [the official leo docs](http://leoeditor.com/leo_toc.html) in Chinese. 

## 如何参与翻译
1. 翻译文章，在 待认领文章列表 中认领翻译文章。回复关键词 认领翻译 即可。

2. 认领翻译通过后，Fork 此仓库, 开始翻译. 注意：Fork 此仓库后，请先从 master 分支上 git checkout -b translate 一个新的 translate 分支来翻译文章，翻译完成后再把 translate 分支发 PR。

3. 翻译完成，发送 Pull Request，PR 的标题为所翻译文章的中文标题，内容请注明对应的 Issue 链接，方便进行管理。: ) 注意：发 PR 的时候请注意检查，一个 PR 只能有一篇文章，切勿两篇或多篇 合并到一个 PR。

4. @OMlalala 校对完成后，会在校对完成时同时 @译者 告知校对完成，译者就可以根据校对者意见进行修改啦，修改完成后 @OMlalala 进行最终检查，merge 后分享你的译文.

## 如何使用 Leo 翻译
- 请先参考 [官方文档: Creating Documents from Outlines](http://leoeditor.com/tutorial-rst3.html)
- 打开主文件: leo-editor-cn/LeoDocs.leo
- 选择感兴趣的文章翻译
- 输入 rst3 命令.
- 移至文档文件夹. `cd leo-editor-cn/html.txt`
- 生成 html 文档. `make html`
- 现在, 翻译后的文档已生成. 可移至 html 文件参考. `cd leo-editor-cn/html`
- 提交一个 pull-request，等待审核.


## Contributors

感谢所有 参与翻译的同学。是大家的开源精神和辛勤工作让文档的翻译得以如此顺利迅速进行。

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

文档翻译采用 <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">知识共享署名-非商业性使用 4.0 国际许可协议</a> 进行许可。著作权归译者本人所有，禁止商用。
