# QUALITY_CHECK — Soyorica Website v2

## 判定

公開用の初期実装として PASS。

前版では「リンク切れがない」「SEOタグがある」「AI的な装飾を避ける」といった最低限の確認に偏っていたため、今回は製品の実在性・購入判断・ドキュメント到達性を評価対象へ追加した。

## 製品提示

- [x] ファーストビューにHairSwayの実際の出力動画を使用した。
- [x] HairSwayのBefore / Afterを動画で提示した。
- [x] Viewer、Inspector、Fusionノードを実際のDaVinci Resolve画面で提示した。
- [x] HairSwayの公式チュートリアルへの導線を商品ページとトップページに設けた。
- [x] HairSway説明書に操作動画の抜粋を追加した。
- [x] MathMotionGraphは数式とCartesian / Parametric / Polarのグラフ例を視覚化した。
- [x] MathMotionGraphの実UI素材がないため、架空のInspector画面を作らず、グラフ例がUIスクリーンショットではないことを明記した。
- [x] Lite / Fullの違いを機能表と実例の両方で説明した。

## 購入・信頼情報

- [x] HairSwayは「販売中」、MathMotionGraph Fullは「近日公開」、Liteは「無料」を明示した。
- [x] HairSwayはDaVinci Resolve 21 Free / Studioを明示した。
- [x] HairSwayのFuse内に記載されたVersion 1.2.3を商品・説明書に表示した。
- [x] MathMotionGraphは確認済み環境（Windows 11 / Resolve 21 Free）と未確認環境を分けた。
- [x] BOOTHの商品ページ・ショップへの導線を設けた。

## ドキュメント

- [x] Docsトップにクライアントサイド検索を追加した。
- [x] HairSway / MathMotionGraphのパラメータ表に絞り込み検索を追加した。
- [x] HairSway基本操作に実UIを追加した。
- [x] MathMotionGraphの数式説明にグラフ例を追加した。
- [x] インストールページをOSタブに分けた。
- [x] インストール先パスをコピーできる。
- [x] FAQをHairSway / MathMotionGraph / Install / Supportで絞り込める。
- [x] FAQはdetails/summaryを使用し、JavaScriptなしでも開閉できる。

## ブランド・デザイン

- [x] Fusionを連想させるポート、接続線、グリッドをSoyoricaの補助的な視覚言語として使用した。
- [x] 抽象的な巨大コピー、ガラス風カード、装飾グラデーションを使用していない。
- [x] 商品メディアを画面の主要面積に配置し、装飾より製品を優先した。
- [x] 既存アイコン由来の濃紺を主色に使用した。
- [x] 日本語・英語の同一ページ間で言語切替を維持する。

## SEO / Accessibility / Technical

- [x] 日本語・英語あわせて18の公開ページ + 404を生成した。
- [x] ページ固有のtitle / description / canonical / hreflangを設定した。
- [x] Home / HairSway / MathMotionGraphに別々のOG画像を用意した。
- [x] BreadcrumbList、SoftwareApplication、FAQPageを該当ページに設定した。
- [x] sitemap.xmlへlastmodを設定した。
- [x] site.webmanifestをHTMLから参照している。
- [x] prefers-reduced-motion時は自動再生動画を停止する。
- [x] 内部リンク、ローカル画像、動画、hreflangターゲットを自動検査した。
- [x] 19 HTML / ERRORS 0 / WARNINGS 0。
- [x] JavaScript構文チェックを通過した。

## 素材不足のため、事実を捏造せず残している課題

以下はサイト側だけでは完全に解消できない。

1. HairSwayの別キャラクター・短髪・服の裾など、異なる素材での実動作例。
2. Protection Pinの「なし / あり」を同じ素材で直接比較する実動画。
3. MathMotionGraphの実際のInspector / Edit / Fusion画面。
4. MathMotionGraph Liteの確定配布URLとFull版の確定販売URL。
5. MathMotionGraphのユーザー向け製品バージョン番号。
6. 両製品の公開可能なリリース履歴、更新方針、ライセンスページ。
7. 実ユーザーの許可を得たレビューや採用事例。

これらはプレースホルダーや架空画像では補っていない。
