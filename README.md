## (1) 程式的功能 Features
基礎的射擊小遊戲，用a d控制左右，空白鍵發射子彈

## (2) 使用方式 Usage
### 1 python環境:
    下載pygame:
    pip install pygame
### 2 使用事項:
    要將輸入法改成英文，否則不會有反應
    a向左，d向右，空白鍵射擊
    碰到飛行物hp-1，hp=0結束
    21、23、24、25、26行中pygame.image.load(os.path.join(資料夾位置，名稱.檔案形式)).convert()來加入圖片
### 3 可修改內容:
    改變目標飛行速度:
        在Rock0、Rock1中改
        self.speed=random.randrange(2,5)改變目標往下的速度
        self.speedx=random.randrange(-4,4)改變目標左右的速度
    改變玩家:
        Player中改 
        self.speed= 左右移速
        self.health= 自訂血量
    改變子彈速度:
        self.speed=random.randrange(-20,-15)
        射擊頻率取決於按空白鍵速度



## (3) 程式的架構 Program Architecture

The project is organized as follows:

```
pygame.init()
    all_splite  將物體放進同個群組
        def rockhit() 將被射到分形物家回群組，因被射擊後會被刪除
    hits=pygame.sprite.groupcollide() 判定碰撞(同群組內物品)
        for i in hits 判定射中飛行物並刪除
            hitrock()將飛行物加回群組
    screen.blit() 將畫面顯示
物體定義:
class 名字(pygame.sprite.Sprite)
    def __init__(self) 寫入給物體的屬性
        pygame.sprite.Sprite.__init__(self)
        寫法如self.image=...
    def update(self) 物體與其他物體或指令輸入時的互動
        寫法同上
     
```

- **Core Components**:
  - `pygame`: 處理視窗的展示以及物件的各種行為(如碰撞、鍵盤的判定)

## (4) 開發過程 Development Process
引入pygame
用pygame製造一個視窗
用class定義玩家、子彈及掉落物的移動及與鍵盤的互動
將視窗內容初始化並增加碰撞的判定、血量計算及分數呈現
導入圖片

## (5) 參考資料來源 References

1. (https://www.youtube.com/watch?v=61eX0bFAsYs&t=6802s) - 定義人物的calss(剩餘物體用類似邏輯完成)及碰撞判定後的處理
2. (https://www.cnblogs.com/gaiqf/articles/16305979.html) - 圖片插入
3. (https://blog.csdn.net/fjswcjswzy/article/details/106102953) - 碰撞判定

## (6) 程式修改或增強的內容 Enhancements and Contributions

### 分數的獲取
1. 新增第二個飛行物
2. 打到其中一個飛行物會加分，另一種會扣分，分數<0遊戲也會結束

### 飛行物移動軌跡:
原本是超出左右邊界便消失，改成反射
