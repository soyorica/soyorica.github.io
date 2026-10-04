# Soyorica Website Design System v2

## 1. 今回の基準

前版の「AI的な装飾を避ける」という禁止中心の設計から、Soyorica固有の製品体験を中心にした設計へ変更する。

公開前の必須条件:

- ファーストビューに実際の製品出力を置く。
- HairSwayでは実動画、Viewer、Inspector、Fusionノードを見せる。
- MathMotionGraphでは数式と対応するグラフ形式を視覚化する。
- 製品説明は「結果 → 操作 → 詳細仕様 → 説明書 → 入手」の順にする。
- マーケティングページとマニュアルを分けるが、相互に直接移動できるようにする。
- 対応確認済み環境と未確認環境を区別する。
- 説明書ではパラメータ検索を提供する。
- FAQは製品・インストール・サポートで絞り込めるようにする。
- 日本語と英語で同じページ構造を用意する。
- SEO、アクセシビリティ、JavaScript無効時の可読性は前版の基準を維持する。

## 2. Visual language

Soyoricaのロゴカラーと、DaVinci Resolve Fusionのノード編集を連想させる「ポート・接続線・薄いグリッド」を共通要素として使う。ただし、装飾だけのノード図を大量に置かず、製品情報や実際の画面へ接続するために使う。

- Navy `#123A53`: 見出し、Primary CTA、主要線
- Secondary navy `#2C5872`: 軸・補助線
- Pale blue `#D9EAF3`: focus、選択、背景補助
- Paper `#F3F6F8`: 全体背景
- Surface `#FFFFFF`: 説明・表・コード領域
- Green `#3F9B7F`: 実動中・販売中・ノードポート
- Orange `#C88442`: MathMotionGraph補助・注意

グラデーション、ガラス風カード、巨大な抽象コピーは使わない。

## 3. Product media

HairSwayの実動画を主要ビジュアルにする。Webでは自動再生動画は muted / loop / playsinline とし、`prefers-reduced-motion`では停止する。説明用スクリーンショットはViewer、Inspector、ノード領域へ分割し、1画像1説明にする。

MathMotionGraphは実UI素材が未提供のため、製品UIのスクリーンショットを捏造しない。代わりに資料で確認できるCartesian / Parametric / Polarの式とグラフ例を「機能例」として表示し、実UIではないことを明記する。

## 4. Typography / layout

- system sans / Japanese system gothic
- body 16px / 1.78
- desktop max-width 1240px
- docs content max-width 900px + 250px sidebar
- 角丸は0–10pxに限定し、カード全面には多用しない
- 製品ページは実メディアを50%以上の視覚面積で扱う

## 5. Documentation

- 左サイドバー + 本文
- 基本操作には実UIを置く
- パラメータ表はテキスト検索可能
- MathMotionGraphは数式例と出力例を対応させる
- インストールはOSタブとコピーボタン
- FAQはカテゴリ絞り込み

## 6. SEO / Accessibility

- 固有title / description / canonical / hreflang
- ページ別OG画像
- BreadcrumbList / SoftwareApplication / FAQPage
- sitemap.xml with lastmod
- 1ページ1 H1
- focus-visibleを保持
- ネイティブdetails/summaryをFAQに利用
- reduced motion対応
