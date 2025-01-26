# ComfyUI-SoX-Mixdown
ComfyUI custom node for sox's mixdown function such as "sox --combine inputfile1.wav inputfile2.wav outputfile.wav".

You can mixdown two same length audio clips to one with this node.

To use this node, let's install the SoX command first ;-)
You can install SoX with following command.

<details>
<summary>Installing Commands</summary>

Windows
```
winget install ChrisBagwell.SoX
```

Mac
```
brew install sox
```

Linux(too many way...)
```
apt install sox
```
```
dnf install sox
```
```
pacman -S sox
```

</details>

Never forget to add "sox" command to your path.

# External Links
## ComfyUI's docs for making and publishing custom nodes
https://docs.comfy.org/custom-nodes/overview

## SoX
https://sourceforge.net/projects/sox/

## pysox
https://github.com/marl/pysox


<details> <summary> <strong> 日本語参考情報 </strong> </summary>

### ComfyUIのカスタムノードを作るには｜にゃおき
https://note.com/nyaoki_board/n/n96ab9293291c

### ComfyUIのコードをまるごとGemini 1.5 Proに読ませてみた😂｜一般オーク
https://note.com/ippan_orc/n/naed830f52f99

### 【西川和久の不定期コラム】NVIDIAがローカルで手軽に動せるAIチャット「Chat with RTX」をリリース！その実力は？ - PC Watch
https://pc.watch.impress.co.jp/docs/column/nishikawa/1571371.html

</details>
いずれかの検索拡張生成（RAG）に ComfyUI のソース一式を読ませると、いい感じにサポートしてくれるかもしれません。
