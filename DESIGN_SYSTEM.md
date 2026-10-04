# Soyorica Website Design System

Version 1.0 / 2026-10-04

## 0. 評価基準

実装前に次の項目を合格条件として固定する。最終実装後も同じ項目で再確認する。

- [x] ファーストビューだけでSoyoricaがDaVinci Resolve / Fusion向けツールを扱うと分かる
- [x] 巨大な一文コピー、意味のないグラデーション、ガラス風カードなど、汎用AIテンプレートに見えやすい表現を使わない
- [x] HairSwayが販売中、MathMotionGraphが近日公開、Lite版が無料であることを誤解なく表示する
- [x] 商品紹介→説明書→インストール→FAQ→購入の導線が2クリック以内で辿れる
- [x] 説明書で基本操作とパラメータリファレンスを分ける
- [x] インストール先パスはクリックでコピーできる
- [x] 日本語を主言語とし、英語ページを独立URLで用意する
- [x] 全ページに固有のtitle、description、canonical、hreflangを設定する
- [x] Product / SoftwareApplication / FAQPage / BreadcrumbListの構造化データを適切なページに入れる
- [x] 本文はJavaScriptなしでも読める静的HTMLにする
- [x] スマートフォンで横スクロールを発生させず、表は必要な場合だけ内部スクロールにする
- [x] WCAG AA相当の本文コントラストを確保し、キーボードフォーカスを見える状態にする
- [x] アニメーションは200ms前後の小さな反応に限定し、prefers-reduced-motionに対応する
- [x] 画像には内容を説明するaltを付け、装飾画像は空altにする
- [x] 第三者フォントに依存せず、初回表示を軽くする
- [x] 将来商品が増えても、Products / Docsの同じ構造を追加して拡張できる

## 1. 参考サイトと採用要素

Awwwards / Webby Awards / FWAで評価される水準を「視覚的に派手であること」ではなく、ブランド固有性、情報設計、操作性、技術完成度の総合基準として扱う。WebbyではBézierが2025年Best Visual Design – Function、iMacが同部門People's Voice、GSAPが2024年Web Services & Applications Winnerとして掲載されている。

| # | Reference | Soyoricaで採用する要素 |
|---:|---|---|
| 1 | [Apple — iMac](https://www.apple.com/imac/) | 商品そのものを主役にし、短い説明と実機ビジュアルで機能を理解させる構成。大見出しだけで成立させず、製品情報の階層を明確にする。 |
| 2 | [Bézier — Build in Amsterdam](https://www.buildinamsterdam.com/) | 装飾を独立させず、ナビゲーションや情報理解に結び付けたビジュアル設計。Webby 2025 Best Visual Design – Function受賞作として機能性を基準にする。 |
| 3 | [Dropbox Brand](https://brand.dropbox.com/) | 色・書体・余白のルールを先に決め、ページごとの差よりブランド全体の一貫性を優先する。 |
| 4 | [Shopify Editions — Summer ’24](https://www.shopify.com/editions/summer2024) | 情報量が多いページで、番号・章立て・カテゴリ見出しを使って現在地を把握しやすくする。 |
| 5 | [GSAP](https://gsap.com/) | 開発者向け製品でも固くしすぎず、ツールの性格が分かる小さな動きと実例を使う。ただしSoyoricaでは演出量を抑える。 |
| 6 | [Google Store](https://store.google.com/) | 商品、比較、購入導線の優先順位が明確。価格や販売状態をCTAの近くに置く。 |
| 7 | [MetaMask Learn](https://metamask.io/learn) | FAQ・ガイドのような情報ページで、カテゴリ分けと検索・絞り込みの考え方を採用する。 |
| 8 | [Linear](https://linear.app/) | 細い罫線、図版番号、短いセクション見出し、製品UIの提示。余白を大きく取るだけでなく、情報の密度を意図的に変える。 |
| 9 | [Raycast](https://www.raycast.com/) | 最初の画面で「何の製品か」「何ができるか」「次に押す場所」を同時に理解できる導線。 |
| 10 | [Framer](https://www.framer.com/) | ページ全体で同じグリッドとタイポグラフィを保ちつつ、各セクションのレイアウトを変える。テンプレート感の強いグラデーション表現は採用しない。 |
| 11 | [Figma](https://www.figma.com/) | 抽象的な装飾ではなく、実際のプロダクト画面や制作物を説明の中心に置く。 |
| 12 | [Rive](https://rive.app/features) | 機能説明を「機能名→何ができるか→実際の画面」の順に見せる。動きは内容を理解するための補助に限定する。 |
| 13 | [ReadMe](https://readme.com/) | 説明書で左サイドバー、本文、コードブロック、パラメータ表を使う情報設計。コピー可能なコード・パス表示も採用する。 |
| 14 | [Blender](https://www.blender.org/download/) | インストール・配布ページでOSや配布形態を先に区別し、迷わず次の操作に進める構成。 |
| 15 | [Vercel](https://vercel.com/) | 高コントラスト、細い罫線、厳密なグリッド。装飾を減らし、技術情報の読みやすさを優先する。 |
| 16 | [FWA 25th Anniversary](https://thefwa.com/FWA25/25.html) | 視覚的な新規性だけでなく、操作と技術の完成度まで評価対象にするという品質基準の参照。 |

## 2. 白黒ワイヤーフレーム

実装前の情報構造は `WIREFRAME.md` と `wireframe.html` に固定した。ここではブランドカラーや影、アニメーションを使わず、見出し階層、導線、製品の優先順位だけを確認する。

### 構成原則

- ファーストビューは「ブランド名」「対象ソフト」「製品一覧への導線」を中心にし、大きな宣伝文句を置かない。
- HairSwayを最初の製品として大きく扱い、MathMotionGraphは近日公開であることを明示する。
- 説明書はマーケティングページと切り分ける。基本操作とリファレンスを同じページ内で章分けし、パラメータ表を探しやすくする。
- インストールは独立ページにし、コピーできるパスを最優先で表示する。
- FAQは質問文そのものが見出しになるアコーディオン形式とし、検索結果から質問へ直接到達しやすくする。

## 3. ブランドカラー

既存Soyoricaアイコンから採った色を基本とする。背景は白系とし、ブランドの濃紺を文字・主要操作に使う。

| Token | Value | Usage |
|---|---|---|
| `--navy-900` | `#11364F` | ロゴ、主要見出し、Primary button |
| `--navy-700` | `#25485F` | 補助線、hover、図版の曲線 |
| `--blue-100` | `#D3E5F0` | ブランドの淡色面、選択状態 |
| `--paper` | `#F7F9FA` | ページ背景 |
| `--white` | `#FFFFFF` | 本文面 |
| `--ink` | `#102733` | 本文 |
| `--muted` | `#5D6B74` | 補足文 |
| `--line` | `#D9E2E8` | 罫線 |
| `--success` | `#19725B` | 販売中の状態表示のみ |

グラデーションは原則使用しない。ブランドアイコン由来の曲線は、1pxの線または背景のごく薄い面としてだけ使う。

## 4. Typography

ロゴがsans serifであるため、見出し・本文もゴシック系で統一する。外部Web Fontは読み込まない。

```css
font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI",
             "Hiragino Sans", "Yu Gothic UI", "Noto Sans JP", sans-serif;
```

- Display: 56px / 1.04 / 700（日本語は48px程度まで。100px級の見出しは使わない）
- H1: 44px / 1.15 / 700
- H2: 30px / 1.3 / 700
- H3: 20px / 1.45 / 700
- Body large: 18px / 1.8
- Body: 16px / 1.8
- Small / UI: 13–14px / 1.5
- Code: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace

英数字だけを極端に細い書体にせず、日本語と混在しても重さが崩れないようにする。

## 5. Layout

- 最大本文幅: 1180px
- 12 column grid / gap 24px
- 左右余白: desktop 32px以上、mobile 20px
- Section間: 96–128px（mobile 64–80px）
- Docs本文: 720–780px
- Docs sidebar: 220px
- Border radius: 0–8px。カードをすべて丸めない。
- 影: 原則なし。浮いていることを示す必要があるポップオーバーだけ使用。

## 6. Components

### Header

白背景、1px下罫線。ブランドマーク＋Soyorica、Products、Manuals、Install、FAQ、BOOTH、言語切替。stickyにするが高さは64px前後に抑える。

### Buttons / Links

Primaryは濃紺の矩形ボタン、Secondaryは背景なし＋1px罫線。角丸は4px。本文中の遷移は「製品を見る →」のようなテキストリンクを優先し、ボタンを乱用しない。

### Product Row

カードのグリッドではなく、罫線で区切った2カラムの「製品行」を使う。左に実物ビジュアル、右に製品名・説明・状態・CTAを置く。

### Status

`販売中 / On sale`、`近日公開 / Coming soon`、`無料 / Free`の3種類。ピル型の大きなバッジにはせず、小さな文字とドットで状態を伝える。

### Code / Path

パスはコードブロック全体をクリック対象にせず、右端に明示的な「コピー」ボタンを置く。コピー成功後は2秒だけ「コピーしました」に変える。

### Documentation table

列は「パラメータ」「初期値」「対象」「説明」。色分けを増やさず、行罫線と太字だけで読む。mobileでは横スクロールを許容する。

### FAQ

`details / summary`を使い、JSなしでも開閉できる。質問文は検索で拾われる自然な文章にする。

## 7. Motion

- hover: 120–180ms
- 大きなパララックス、スクロール固定、カーソル追従は使わない。
- Product imageはhover時に最大2pxだけ移動してよい。
- `prefers-reduced-motion: reduce`ではtransitionを無効化する。

## 8. Copy style

- 「制作を次のレベルへ」のような抽象コピーを避け、機能をそのまま書く。
- HairSway: 「髪・リボン・服の裾などを、キーフレームなしで自動的に揺らす」
- MathMotionGraph: 「数式からグラフを描き、透明背景で映像に重ねる」
- 販売状況や対応環境は断定できる範囲だけを書く。
- 製品ページは「何ができるか→誰向けか→主な機能→説明書→入手」の順。

## 9. SEO / IA

### URL

- `/` 日本語トップ
- `/products/` 製品一覧
- `/products/hairsway/`
- `/products/mathmotiongraph/`
- `/docs/`
- `/docs/hairsway/`
- `/docs/mathmotiongraph/`
- `/install/`
- `/faq/`
- `/en/...` 英語版

### Technical SEO

- 1ページ1つのH1
- 固有title / meta description
- canonical / `hreflang="ja"`, `hreflang="en"`, `x-default`
- Open Graph / Twitter card
- `sitemap.xml`, `robots.txt`
- SoftwareApplication / Product / FAQPage / BreadcrumbList JSON-LD
- 重要本文をJS生成しない
- 画像のwidth/heightを明示してCLSを抑える

## 10. Accessibility

- focus-visible: 3pxの淡青アウトライン
- 本文色 `#102733` × 白背景を基本にする
- 44px程度のタップ領域を確保
- 状態を色だけで区別しない
- `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`を適切に使う
- FAQはbuttonではなく`summary`でネイティブ操作可能にする

## 11. 実装後セルフチェック

最終実装に対し、自動チェックと目視確認を行った結果を `QUALITY_CHECK.md` に残す。未達項目がある状態では公開版としない。
