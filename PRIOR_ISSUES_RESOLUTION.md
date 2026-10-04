# 前版で指摘した課題への対応

| 前版の課題 | v2の対応 |
|---|---|
| ファーストビューに製品の実物がない | HairSway実動動画をHeroに配置 |
| HairSwayの「揺れる」が静止画でしか分からない | 実動画とBefore / After動画を使用 |
| Viewer上のピンが見えない | 実スクリーンショットからViewer領域を切り出して説明 |
| Inspectorが見えない | 実Inspectorを機能説明へ配置 |
| Fusionノード構成が見えない | 実ノード画面をワークフローへ配置 |
| 製品ページがテキストカード中心 | 結果→実UI→機能→Compatibility→Docs/購入の順に再構成 |
| MathMotionGraphが小さなアイコンしかない | Cartesian / Parametric / Polarのグラフ例を大きく提示 |
| MathMotionGraphのLite / Full差が表だけ | グラフ種別の実例 + 比較表へ変更 |
| デザインが一般的なミニマルSaaSに寄っていた | Fusion由来のポート、接続線、グリッドを共通言語に採用 |
| 禁止事項中心のデザインシステム | 「製品を実物で見せる」を最上位ルールへ変更 |
| Docsの巨大パラメータ表が探しにくい | パラメータ絞り込み検索を追加 |
| Docsに実画面がない | HairSwayに実UIと操作動画抜粋を追加 |
| Docs全体を検索できない | Docsトップに検索を追加 |
| InstallでOS情報が縦に長い | Windows / macOS / Linuxタブへ変更 |
| FAQが一列で混在 | カテゴリ絞り込みを追加 |
| 確認済み環境と未確認環境が曖昧 | MathMotionGraphの商品ページで明示 |
| 言語切替がトップへ戻る | JavaScriptで同一パスの日英ページへ切替 |
| 全ページ同じOG | Home / HairSway / MathMotionGraphで個別作成 |
| BreadcrumbListが設計だけで実装されていない | 該当ページへJSON-LDを実装 |
| site.webmanifestが未参照 | `<link rel="manifest">`を追加 |
