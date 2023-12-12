<div align=center>
<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/067683fb-5d66-4cde-b461-5b192440b448" width="1000"></div>
 
# League Of Lengend 게임 데이터 승패 예측 프로젝트 
Riot Games에서 제공하는 LOL 랭크 게임 데이터를 활용한 게임 승패 예측 프로젝트
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>

</div>

# 1. 개요 


League of Legends(이하 LoL)은 라이엇 게임즈가 개발 및 서비스 중인 MOBA(Multiplayer Online Battle Arena) 장르의 게임으로, 5명의 플레이어가 각자 다른 포지션에서 성장을 통해 아이템과 레벨을 올려 상대의 기지를 파괴하는 게임이다. 이 게임은 MOBA(AOS) 장르의 이전 게임들과는 다르게 진입 장벽이 낮아 더 많은 인기를 얻고 있으며 전 세계적으로 많은 유저들을 보유하고 있다.
<a href="https://www.hani.co.kr/arti/culture/culture_general/1066200.html/">[1]</a> 

2016년 기준으로 월 플레이어 수가 1억 명 이상을 기록하며, 2019년 8월에는 전 세계 서버의 피크 시간 동시 접속자 수가 800만 명 이상이었다. 
또한 League of Legends은 전 세계 E스포츠 대회에서 가장 많은 시청자 수를 기록하며, 리그 오브 레전드 월드 챔피언십과 각 지역 리그 등 다양한 e스포츠 대회가 개최되는 중이다.
2018 자카르타·팔렘방 아시안 게임에서는 공식 시범 종목으로 채택되기도 했다. <a href="https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C%20%EC%9B%94%EB%93%9C%20%EC%B1%94%ED%94%BC%EC%96%B8%EC%8B%AD/">[2]</a>
국내에서는 League of Legends가 PC방 점유율 1위를 유지하며 대한민국 청소년 문화의 상징 중 하나로 자리매김하고 있으며 특히 청소년과 젊은 성인층을 중심으로 꾸준한 인기를 누리고 있다.
<a href="https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%ED%9D%A5%ED%96%89/">[3]</a>
<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/1cbe21b1-de65-47d6-8790-ea9863818a56" width="300"></div>
 (출처:<a href="https://www.gametrics.com/">gametrics</a>) </p></h5>

LOL을 개발한 Riot Games는 게임 자체의 재미뿐만 아니라 분석 가능한 데이터를 무료로 공개하고 있다.
Riot Games API를 통해 LOL 소환사의 개인 게임 정보와 함께 경기 데이터까지 제공되고 있으며 <a href="https://developer.riotgames.com/">[4]</a> LOL 공식 홈페이지에서 플레이어의 통계 메뉴에서 자신이 다른 플레이어에 비해 뛰어난 부분과 연패 시의 문제점을 직접 분석해볼 수도 있다.

![image](https://github.com/yeon0306/LOL_project/assets/112537146/4fdb039d-5f70-4d87-a358-2be17bad781c) <br>
 (출처: <a href="https://www.inven.co.kr/board/lol/2778/59746">LOL inven</a>) </p></h5>

통계적으로 하루 24시간 동안 수집되는 경기 수는 약 20만 건에 달하며, 
소정의 절차를 거치면 손쉽게 얻을 수 있다.<a href="https://dev-records.tistory.com/entry/Python-Riot-API-LOL-%EB%9E%AD%ED%81%AC-%EA%B2%8C%EC%9E%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91/">[5]</a>
이번 프로젝트에서는 20만 건의 하루치 LOL 게임 데이터를 분석하여 승패를 예측하는 모델을 만들어 보고자 한다.


# 2. 데이터
# 2.1 데이터 소스

이번 프로젝트에 활용할 데이터는 온라인 게임 코칭 전문기업인 
더매치랩(The Match LAB)에서 가공한 LOL 게임 데이터를 바탕으로 한다.
데이터는 2023년 8월 25일, 9월 15일, 9월 17일 각각 하루 동안 수집된 
LOL 경기에 대한 세부 항목들로 구성되어 있다.

## 2.2 탐색적 데이터 분석

데이터는 5대5 솔로 랭크 경기 약 20만 건으로 구성되어 있으며 포지션별로 데이터가 구분되어 있다. 

스킬의 메커니즘에 따라 운용법이 나뉘는 6가지(암살자,탱커,전사,마법사,원거리딜러,서포터)의 '역할군'과 별도로 초중반에 담당하는 공격로에 따라 결정되는 '포지션'이라는 개념이 존재한다.
초창기에는 유저들이 사용하는 전술들 중 하나였으나 라이엇이 차후 EU 스타일 체제를 인정하면서 라이엇 공식으로 자리잡는다.
기본적인 구성은 상단 공격로(Top Lane) 1명, 정글(Jungle) 1명, 중단 공격로(Mid Lane) 1명, 하단 공격로(Bottom Lane) 2명으로 이루어진다. 
5가지 포지션에 대한 내용은 다음과 같다.

<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/74c247e5-7674-4bcc-bb8d-15a0ee01b9d5" width="700"></div>

| 포지션 | 위치 | 역할 | 설명 |
|-------|-----|----|-----|
|탑(TOP)|상단라인|라인교전,스플릿 푸시|탑 라인은 가장 윗라인을 말하며 개인의 실력이 가장 크게 영향을 받는 포지션이다. 탑 라인에서는 챔피언의 종류에 따라 1레벨 교전이나 3레벨 교전에서 승부가 결정되는 경우가 많으며 한 번 승부가 갈리면 역전하기 어려운 상황이 있다. 이러한 경우에는 정글의 도움을 받아 라인전에서 우세를 가져와야 하는데 탑은 정글의 도움을 받기가 가장 어렵다. 그러나 탑에서 우위를 점하는 경우 끊임없이 상대 탑라이너를 성장하지 못하게 하는 사이드운영에 유리하다. 반대로 팀이 지고 있는 경우에도 탑 라인은 사이드 운영을 통해 변수를 창출하기 좋은 라인이다.
|정글(JUG)|중립지역,전체라인|정글링,갱킹|게임 중 가장 바쁘고 신속한 결정이 필요한 포지션이다. 기본적으로 아군 진형의 정글 몬스터를 사냥하여 경험치를 얻으며 성장하고 불리한 라인에 갱킹을 가하거나 유리한 라인을 더 강화한다. 뿐만 아니라 오브젝트 싸움에서도 활약이 요구된다. 정글 포지션이 수행해야 할 것은 매우 다양하고 변수가 많다. 내 챔피언과 상대 정글 챔피언 간의 구조를 이해해야 하며 상대 정글의 위치를 지속적으로 예측하고 동선을 체크해야한다. 또한, 팀 내 어느 라인이 공격을 받을지를 예측하고, 이에 따른 결과를 고려하는 플레이가 필요하다. 정글의 플레이에 따라 어려운 부분이 쉬워지기도 하고, 쉬운 부분이 어려워지기도 한다.
|미드(MID)|중단라인|로밍,AP딜러,AD딜러|미드 라인은 팀 내에서 가장 막중한 책임을 지는 포지션이다. 미드 라인에서 플레이 가능한 챔피언의 폭은 넓으며 이에 따른 운영 및 교전 전략도 매우 다양하다. 현재 롤의 메타가 빠른 진행 속도로 인해 탑이나 바텀으로 로밍해야 하는 경우가 빈번하게 발생하며 정글 간의 교전에도 신속하게 대응해야 한다.
|원딜(ADC)|하단라인|AD딜러,포킹|원딜은 게임 내에서 원거리 딜러를 가리키는 용어로, 전체 딜 중에서 가장 큰 영향을 미치는데 동시에 체력이 매우 낮아 신중한 플레이가 필요하다. 챔피언에 따라 생존기의 유무가 갈리며 이에 따라 한타 교전 시 포지셔닝도 다양하다. 후반 운영에서 원딜의 성장 차이에 따라 팀의 승패가 결정되는 경우가 많다.
|서폿(SPT)|하단라인|탱킹,이니시에이팅,로밍|서포터는 원딜이 원활하게 성장할 수 있도록 도우며, 바텀 교전 중에는 서폿의 실력과 챔피언에 따라 성장 방식을 결정한다.라인전에서 일반 라이너들이 끊임없이 CS를 먹어야 하는 반면, 서포터는 전용 아이템으로 정해진 시간마다 소량의 CS만 챙기면 된다. 따라서 남는 시간동안 교전, 딜각제기, 맵 리딩 등 다양한 부수적인 역할이 요구된다.

*AD : 물리 공격력 (Attack Damage)* </br>
*AP : 마법 공격력 (Ability Power)* </br> 
*로밍 : 라인 주도권을 가진 라이너가 아군을 돕기위해 다른 라인에 개입 하는 행위* </br>
*스플릿 : 아군의 상황과 맞춰 지속적으로 라인 관리를 해주면서 기회가 됐을때 포탑 철거를 하는 행위* </br>
*포킹: 상대에게 원거리 스킬을 지속적으로 날려 상대에게 체력적 압박을 가하는 행위* </br>

제공된 데이터의 항목은 총 185개로 구성되어 있으며 전반적으로 다음과 같은 내용으로 정리해볼 수 있다.

| 항목          |데이터 속성 |
|-------------|---------|
| 플레이어에 대한 데이터|tier,kills,deaths,assists,cs,xp...|
| 팀에 대한 데이터 |baron,dragon,goldearned,dratio,gratio...|
| 라인전 전후에 대한 데이터 |assist_at14,cs_at14,cs_af14,death_at14...|

여기서 중요하게 고려되는 항목들은 다음과 같다. 

| 데이터 속성 | 데이터의 의미 | 중요한 이유 |
|-------------|---------|--------|
| tier | 티어 | 티어는 플레이어의 게임 실력을 종합적으로 나타내는 중요한 지표이다. 게임 내 전략 이해도, 챔피언 조작 능력, 팀워크 등을 바탕으로 하며 플레이어들 간의 실력 차이를 확인할 수 있다. |
| dealt | 챔피언에게 넣은 데미지 | 플레이어들 간의 상대적인 역량을 비교하는 데 도움 된다. 높은 데미지를 기록한 플레이어는 자신의 역할을 효과적으로 수행하는 것으로 판단할 수 있다. | 
| goldearned | 총 획득 골드 | 골드는 챔피언의 성장을 위한 주요 자원이다. 적을 처치하거나 미니언 처치, 오브젝트 파괴, 포탑 파괴 등의 활동을 통해 골드를 획득하여 상위 아이템을 구매하고 강화하며 전투 능력을 크게 향상시킨다. 따라서 골드 획득량은 챔피언의 성장 속도와 직결되며 게임 내에서 얼마나 빠르게 우위를 점하고 있는지 판단하는 중요한 지표가 된다. |
| GPM | Gold Per Minute (분 당 획득 골드)| 플레이어가 매 분마다 얼마나 많은 골드를 획득하는지 측정하는 지표이다. 골드는 아이템 구매와 발전에 중요한 역할을 하므로 GPM이 높은 플레이어는 상대 플레이어에 비해 더 빠르게 성장하고, 전투에서 유리한 위치를 점할 수 있다.
| KDA | Kill/Death/Assist의 비율 | 킬은 상대방을 처치한 횟수, 데스는 죽은 횟수, 어시스트는 팀원이 상대를 처치하는데 도움을 준 횟수를 의미하며 이를 종합해 플레이어의 게임 내 활약도를 판단할 수 있다.|
| DPM | Damage Per Minute (분 당 가한 데미지) | 플레이어가 상대 플레이어, 미니언, 중립 몬스터 등에게 가하는 피해의 양을 분당으로 계산한 지표이며 플레이어의 공격력과 전투 참여 정도를 파악할 수 있다. 일부 챔피언은 초기에는 공격력이 낮아 DPM이 낮을 수 있지만, 플레이어가 선택한 아이템 빌드와 스킬 사용 방식에 따라 증가할 수 있으며 높은 DPM을 유지하는 플레이어는 팀의 승리에 기여 할 수 있다.| 
| DPD | Damage Per Death (데스당 가한 데미지)| 플레이어가 죽을 때마다 얼마나 많은 피해를 입혔는지 나타내는 지표이며 플레이어의 전투력과 생존력을 파악할 수 있다. 예를 들어 플레이어가 높은 데미지를 기록하고 적게 죽었다면 효율적으로 피해를 입히고 생존하는 능력이 뛰어나다고 볼 수 있다.|
| DPG | Damage Per Gold (골드당 가한 데미지)| 챔피언에게 넣은 데미지와 총 사용골드를 나타내는 지표이며 골드 소모량과 그에 따른 데미지를 파악하여 플레이어의 경기력과 팀의 승리 가능성을 예측하는데 도움이 된다. 예를 들어, 특정 챔피언의 DPG 가 상대 챔피언보다 높다면 효율적인 데미지를 주고 있는지 판단할 수 있다.|
| DTPM | Damage Taken Per Minute (분당 받은 피해량) | 매 분마다 얼마나 많은 피해를 받는지를 측정하는 지표로, death와 함께 볼 수 있다. 플레이어의 생존력과 탱크 역할을 수행하는 챔피언의 효율성을 판단하는데 사용될 수 있다. 따라서 DTPM 이 높으며 데스가 낮다면 탱커 챔피언이 얼마나 효과적으로 상대의 공격을 받고 있는지를 평가하는 지표로 활용된다. |
| XPM | Experience Per Minute (분당 획득 경험치) | 분당 경험치 획득량을 나타내는 지표로, 플레이어가 게임 진행 중에 얼마나 경험치를 획득하는지 볼 수 있다. 경험치를 얻기 위해서는 적의 챔피언, 미니언, 오브젝트 등을 처치해야한다. 따라서 플레이어의 레벨과 분당 경험치 획득량을 보고 게임의 흐름을 예측할 수 있다. |


## 2.3 데이터 전처리

20만 건의 경기 데이터는 수준 별로 편차가 어느정도 존재할 것으로 
예상된다. 따라서 일정 수준 이상의 데이터로 지표의 상관성을 통해
승패예측 모델을 만드는 것이 합리적일 것이다.

이에 이번 프로젝트에서는 다음과 같이 정의되는 LOL게임의 등급체계(tier)
를 바탕으로, 모든 플레이어가 플래티넘 이상인 경기를 추출하여 분석해보고자 한다.

* 티어에 대한 정보 (표)
* 티어별 히스토그램
* 플래티넘 이상인 경기의 수

도출된 플래티넘 이상의 경기에 대해서, 핵심 데이터 속성으로 
???, ???, ??? 등을 추출했다. 그 이유는 ~~~ 때문이다. 그리고 승패를 
예측하는 것이기 때문에, 경기 데이터를 기준으로 데이터 속성별 정규화
(normalize)를 수행했다.


## 2.4 데이터 프레임 설계 

| id | team | feature |  TOP | MID | JUG | SPT | ADC | 
|---| ---| --------|---------|----|-----|----------|-----------|
|고유번호 | 100(blue) | kda   | 0.333333  | 0.4 | 0.416667 | 1.83333 |  4.0 |
|          |          | dpd   | 2706.5  | 2024.0  | 1029.08  |2925.33  | 6254.0 |
|          |          | dpm   | 506.151 | 315.429 |  384.904 | 547.075 |  584.79 |
|          |          | dpg   | 1.75178 | 1.09052 |  1.44687 | 1.96882 | 1.23727 |
|          |          | dtpm  | 1376.23 | 645.569 |  1308.37 | 717.101 | 588.81 |
|          |          | win   |    0   |   0   |   0    |    0    |    0  |
|          |          | tier  |   E      |   P    |  E     |   P    |    P |
| .....    |  ...     |   ...   |    ...    |    ...     |     ...      |    ...       |    ...      | 
| 고유번호  |  200(red) |   kda   |      3.0    |   1.5    |     7.0      |  8.0   |  4.6 | 
|           |           |   dpd   |    4528.0  | 2562.33   |  6408.0  |  2513.33    | 6971.6 | 
|           |           |   dpm   |  534.803   |  605.276  | 756.85   |  296.85    |  1372.36 | 
|           |           |    dpg  |  1.47332   |  1.49117  | 1.82149  |    1.006   |  2.68759 | 
|           |           |   dtpm  |  606.654   |  771.732  |  1094.92  |  623.189  | 563.543  | 
|           |           |   win   |      1     |     1     |     1     |     1    |    1   | 
|           |           |   tier  |     P      |    P      |     P    |    G    |    P   |    
 





# 3. 승패예측 모델 


|   |    |  정확도(단순) | 정확도(cnn)| 
|---| ---| --------|-----|
|0825|플래티넘↑| 95% |   |
|    | 전체 |    |   |
|0915|플래티넘↑| 93.4% |     |
|    | 전체  |       |      |
|0917|플래티넘↑| 88.4% |     |


## 3.1 모델 개요
CNN을 썼다. 단순한 합산을 썼다.

## 3.2 성능
0825
0915
0917
플래티넘 이상 4.5만건
데이터 전체 20만건

## 3.3 소결 
* 성능에 대한 의미 

