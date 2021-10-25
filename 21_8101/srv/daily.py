#2021/10/18 優化完基本對話功能。待安裝:視覺機能(多緒1)、聽覺機能(多緒2)、發聲機能(實驗性多緒1)

import property.Property

def general_dialog():
    while True:
        property.Property.User.speak()
        property.Property.local_system.speak()

