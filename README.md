<div align=center>
<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/067683fb-5d66-4cde-b461-5b192440b448.PNG" width="1000"></div>
 
# League Of Lengend 게임 데이터 승패 예측 프로젝트 
더매치랩(The Match LAB)에서 가공한 LOL 랭크 게임 데이터를 활용한 게임 승패 예측 프로젝트

<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
</div>

# 1. 개요 


League of Legends(이하 LoL)은 라이엇 게임즈가 개발 및 서비스 중인 MOBA(Multiplayer Online Battle Arena) 장르의 게임으로, 5명의 플레이어가 각자 다른 포지션에서 성장을 통해 아이템과 레벨을 올려 상대의 기지를 파괴하는 게임이다. 이 게임은 MOBA(AOS) 장르의 이전 게임들과는 다르게 진입 장벽이 낮아 더 많은 인기를 얻고 있으며 전 세계적으로 많은 유저들을 보유하고 있다.
<a href="https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%ED%9D%A5%ED%96%89">[1]</a> 

2016년 기준으로 월 플레이어 수가 1억 명 이상을 기록하며, 2019년 8월에는 전 세계 서버의 피크 시간 동시 접속자 수가 800만 명 이상이었다. 
또한 League of Legends은 전 세계 E스포츠 대회에서 가장 많은 시청자 수를 기록하며, 리그 오브 레전드 월드 챔피언십과 각 지역 리그 등 다양한 e스포츠 대회가 개최되는 중이다.
2018 자카르타·팔렘방 아시안 게임에서는 공식 시범 종목으로 채택되기도 했다. <a href="https://namu.wiki/w/2018%20%EC%9E%90%EC%B9%B4%EB%A5%B4%ED%83%80%C2%B7%ED%8C%94%EB%A0%98%EB%B0%A9%20%EC%95%84%EC%8B%9C%EC%95%88%20%EA%B2%8C%EC%9E%84/e%EC%8A%A4%ED%8F%AC%EC%B8%A0/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EB%B3%B8%EC%84%A0">[2]</a>
국내에서는 League of Legends가 PC방 점유율 1위를 유지하며 대한민국 청소년 문화의 상징 중 하나로 자리매김하고 있으며 특히 청소년과 젊은 성인층을 중심으로 꾸준한 인기를 누리고 있다.
<a href="https://www.mk.co.kr/news/it/10342621">[3]</a>


<div>
  <img src="https://github.com/yeon0306/LOL_project/assets/112537146/965fda30-b7ea-4f52-a6b1-39c93d193fad" width="200">
  <img src="https://github.com/yeon0306/LOL_project/assets/112537146/057132e5-c62f-41c9-8cb0-b569fd7d60f8" width="600">
</div>

 (출처: [gametrics](https://www.gametrics.com/)  ,  [gameple](https://www.gameple.co.kr/news/articleView.html?idxno=143043))


LOL을 개발한 Riot Games는 게임 자체의 재미뿐만 아니라 분석 가능한 데이터를 무료로 공개하고 있다.
Riot Games API를 통해 LOL 소환사의 개인 게임 정보와 함께 경기 데이터까지 제공되고 있으며 <a href="https://developer.riotgames.com/">[4]</a> LOL 공식 홈페이지에서 플레이어의 통계 메뉴에서 자신이 다른 플레이어에 비해 뛰어난 부분과 연패 시의 문제점을 직접 분석해볼 수도 있다.

통계적으로 하루 24시간 동안 수집되는 경기 수는 약 20만 건에 달하며, 
소정의 절차를 거치면 손쉽게 얻을 수 있다.<a href="https://dev-records.tistory.com/entry/Python-Riot-API-LOL-%EB%9E%AD%ED%81%AC-%EA%B2%8C%EC%9E%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91/">[5]</a>
이번 프로젝트에서는 20만 건의 하루치 LOL 게임 데이터를 분석하여 승패를 예측하는 모델을 만들어 보고자 한다.


# 2. 데이터
# 2.1 데이터 소스

이번 프로젝트에 활용할 데이터는 온라인 게임 코칭 전문기업인 
더매치랩(The Match LAB)에서 가공한 LOL 랭크 게임 데이터를 바탕으로 한다.
데이터는 2023년 8월 25일, 9월 15일, 9월 17일 각각 하루 동안 수집된 
LOL 경기에 대한 세부 항목들로 구성되어 있다.

## 2.2 탐색적 데이터 분석

데이터는 5대5 솔로 랭크 경기 약 20만 건으로 구성되어 있으며 포지션별로 데이터가 구분되어 있다. 

스킬의 메커니즘에 따라 운용법이 나뉘는 6가지( 암살자, 탱커, 전사, 마법사, 원거리딜러, 서포터) 의 '역할군'과 별도로 초중반에 담당하는
공격로에 따라 결정되는 '포지션' 이라는 개념이 존재한다. 초창기에는 유저들이 사용하는 전술들 중 하나였으나 라이엇이 차후 EU 스타일 체제를 인정하면서 라이엇 공식으로 자리잡는다.
기본적인 구성은 상단 공격로(Top Lane) 1명, 정글(Jungle) 1명, 중단 공격로(Mid Lane) 1명, 하단 공격로(Bottom Lane) 2명으로 이루어진다. </br>

5가지 포지션에 대한 내용은 다음과 같다.

<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/74c247e5-7674-4bcc-bb8d-15a0ee01b9d5" width="500"></div>

| 포지션 | 위치 | 역할 | 설명 |
|-------|-----|----|-----|
|탑(TOP)|상단라인|라인교전,스플릿 푸시|개인의 실력이 가장 크게 영향을 받는 포지션이다.챔피언의 종류에 따라 1레벨 교전이나 3레벨 교전에서 승부가 결정되는 경우가 많으며 한 번 승부가 갈리면 역전하기 어려운 상황이 있다. 이러한 경우에는 정글의 도움을 받아 라인전에서 우세를 가져와야 하는데 탑은 정글의 도움을 받기가 가장 어렵다. 그러나 탑에서 우위를 점하는 경우 끊임없이 상대 탑라이너를 성장하지 못하게 하는 사이드운영에 유리하다. 반대로 팀이 지고 있는 경우에도 사이드 운영을 통해 변수를 창출하기 좋은 라인이다. | 
|정글(JUG)|중립지역,전체라인|정글링,갱킹|게임 중 가장 바쁘고 신속한 결정이 필요한 포지션이다. 기본적으로 아군 진형의 정글 몬스터를 사냥하여 경험치를 얻으며 성장하고 불리한 라인에 갱킹을 가하거나 유리한 라인을 더 강화한다. 내 챔피언과 상대 정글 챔피언 간의 구조를 이해해야 하며 상대 정글의 위치를 지속적으로 예측하고 동선을 체크하며 팀 내 어느 라인이 공격을 받을지를 예측하고, 이에 따른 결과를 고려하는 플레이가 필요하다.|
|미드(MID)|중단라인|로밍,AP딜러,AD딜러|팀 내에서 가장 막중한 책임을 지는 포지션이다. 미드 라인에서 플레이 가능한 챔피언의 폭은 넓으며 이에 따른 운영 및 교전 전략도 매우 다양하다. 현재 롤의 메타가 빠른 진행 속도로 인해 탑이나 바텀으로 로밍해야 하는 경우가 빈번하게 발생하며 정글 간의 교전에도 신속하게 대응해야 한다. |
|원딜(ADC)|하단라인|AD딜러,포킹|원딜은 게임 내에서 원거리 딜러를 가리키는 용어로, 전체 딜 중에서 가장 큰 영향을 미치는데 동시에 체력이 매우 낮아 신중한 플레이가 필요하다. 챔피언에 따라 생존기의 유무가 갈리며 이에 따라 한타 교전 시 포지셔닝도 다양하다. 후반 운영에서 원딜의 성장 차이에 따라 팀의 승패가 결정되는 경우가 많다.  |
|서폿(SPT)|하단라인|탱킹,이니시에이팅,로밍|서포터는 원딜이 원활하게 성장할 수 있도록 도우며 바텀 교전 중에는 서폿의 실력과 챔피언에 따라 성장 방식을 결정한다. 라인전에서 일반 라이너들이 끊임없이 CS를 먹어야 하는 반면, 서포터는 전용 아이템으로 정해진 시간마다 소량의 CS만 챙기면 된다. 따라서 남는 시간동안 교전, 딜각제기, 맵 리딩 등 다양한 부수적인 역할이 요구된다.  |


*AD : 물리 공격력 (Attack Damage)* </br>
*AP : 마법 공격력 (Ability Power)* </br> 
*로밍 : 라인 주도권을 가진 라이너가 아군을 돕기위해 다른 라인에 개입 하는 행위* </br>
*스플릿 : 아군의 상황과 맞춰 지속적으로 라인 관리를 해주면서 기회가 됐을때 포탑 철거를 하는 행위* </br>
*포킹: 상대에게 원거리 스킬을 지속적으로 날려 상대에게 체력적 압박을 가하는 행위* </br>


제공된 데이터의 항목은 총 185개로 구성되어 있으며 전반적으로 다음과 같은 내용으로 정리해볼 수 있다.

| 항목    | 데이터 속성 |
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

20만 건의 경기 데이터는 수준 별로 편차가 어느정도 존재할 것으로 예상된다.따라서 일정 수준 이상의 데이터로 지표의 상관성을 통해 승패예측 모델을 만드는 것이 합리적일 것이다.

이에 이번 프로젝트에서는 다음과 같이 정의되는 LOL게임의 등급체계(tier) 를 바탕으로, 모든 플레이어가 **플래티넘 이상**인 경기를 추출하여 분석해보고자 한다.

<details>
<summary>한국 티어 분포표 </summary>
<div><img src="https://github.com/yeon0306/LOL_project/assets/112537146/91d2b568-1b73-4049-92f6-b7064f3eaf50" width="500"></div>
 
<div markdown="1">
<table>
  <tr><th>티어</th><th>단계</th><th>분포</th><th>합</th></tr>
  <tr><th rowspan='1'>챌린저</th><th>I</th><td>0.01%</td><td>0.01%</td></tr>
  <tr><th rowspan='1'>그랜드마스터</th><th>I</th><td>0.02%</td><td>0.03%</td></tr>
  <tr><th rowspan='1'>마스터</th><th>I</th><td>0.47%</td><td>0.50%</td></tr>
   <tr><th rowspan='4'>다이아</th><th>I</th><td>0.39%</td><td rowspan='4'>3.45%</td></tr>
  <tr><th>II</th><td>0.55%</td></tr>
  <tr><th>III</th><td>0.69%</td></tr>
   <tr><th>IV</th><td>1.82%</td></tr>
    <tr><th rowspan='4'>에메랄드</th><th>I</th><td>1.58%</td><td rowspan='4'>13.66%</td></tr>
  <tr><th>II</th><td>1.93%</td></tr>
  <tr><th>III</th><td>3.2%</td></tr>
   <tr><th>IV</th><td>6.95%</td></tr>
    <tr><th rowspan='4'>플래티넘</th><th>I</th><td>2.15%</td><td rowspan='4'>16.96%</td></tr>
  <tr><th>II</th><td>3.22%</td></tr>
  <tr><th>III</th><td>4.2%</td></tr>
   <tr><th>IV</th><td>7.39%</td></tr>
    <tr><th rowspan='4'>골드</th><th>I</th><td>2.68%</td><td rowspan='4'>19.25%</td></tr>
  <tr><th>II</th><td>3.92%</td></tr>
  <tr><th>III</th><td>4.84%</td></tr>
   <tr><th>IV</th><td>7.81%</td></tr>
    <tr><th rowspan='4'>실버</th><th>I</th><td>2.78%</td><td rowspan='4'>19.03%</td></tr>
  <tr><th>II</th><td>4.01%</td></tr>
  <tr><th>III</th><td>4.87%</td></tr>
   <tr><th>IV</th><td>7.37%</td></tr>
    <tr><th rowspan='4'>브론즈</th><th>I</th><td>3.3%</td><td rowspan='4'>19.92%</td></tr>
  <tr><th>II</th><td>4.49%</td></tr>
  <tr><th>III</th><td>5.08%</td></tr>
   <tr><th>IV</th><td>7.05%</td></tr>
    <tr><th rowspan='4'>아이언</th><th>I</th><td>3.11%</td><td rowspan='4'>7.21%</td></tr>
  <tr><th>II</th><td>2.54%</td></tr>
  <tr><th>III</th><td>1.08%</td></tr>
   <tr><th>IV</th><td>0.48%</td></tr>
</table> <br>
</div>

티어는 승리하여 일정한 LP를 모으면 다음 티어로 승급하거나, 패배하여 LP를 잃으면 강등된다. 아이언부터 브론즈, 실버, 골드, 플래티넘, 에메랄드, 다이아, 마스터, 그랜드마스터 그리고 마지막 랭크인 챌린저까지 존재하며 아이언 랭크에는 아이언4부터 아이언 1까지의 티어가 있고, 이는 다이아 랭크까지 동일한 체제를 갖추고 있다. 숫자가 낮을 수록 낮은 티어이며 숫자가 높을수록 상위 티어로 분류된다. 그 위에 있는 마스터, 그랜드 마스터, 챌린저는 점수제로 바뀐다. 
</details>

<details>
<summary>0825 전체 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/4a40c073-cedd-4504-ba8f-be2e81edcae9"> </div>
</details>

<details>
<summary>0825 플래티넘 이상 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/c2b0d636-4726-4de2-9e99-45d6a993afcd"> </div>
</details>

<details>
<summary>0915 전체 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/e87da1c9-001e-43d7-8989-f5e657f2cc63"> </div>
</details>

<details>
<summary>0915 플래티넘 이상 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/40e8ecab-2f38-4cfb-ba09-d0271eea180d"> </div>
</details>

<details>
<summary>0917 전체 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/6bc8974a-b73a-4b7e-ae62-d2df0fc8d545"> </div>
</details>

<details>
<summary>0917 플래티넘 이상 티어 분포도</summary>
<div align="left"><img src="https://github.com/yeon0306/LOL_project/assets/112537146/8203f5d8-fc24-4770-b67e-e381736ba009"> </div>
</details>


* 플래티넘 이상인 경기의 수
  
|  |	0825	|0915|	0917|
|--| ---- |----|-----|
|플래티넘↑ |44962|	28209|	25208|

플래티넘 이상의 경기에서 핵심 데이터 속성으로 **kda, dealt, dpm, dpg, dpd, dtpm, goldearned, kills, object, diffdpg, diffcs, gpm, xpm** 을 추출했다. 각 속성은 플레이어의 성과, 팀의 성과, 경기의 흐름 등 다양한 각도에서 종합적으로 나타내기 위해 선택했다. KDA는 플레이어의 종합적인 성과 지표이며, DPM은 지속적인 활약과 피해량 효율을, DPG는 피해량과 획득 골드의 관계를, DPD는 죽음과 입힌 피해량을 나타낸다. Kills는 킬 수를 통해 공격적인 플레이를 측정하고, Object는 오브젝트 통제 여부를 확인할 수 있다. 또한 각 팀의 피해량과 골드 격차를 나타낸 DiffDPG와 DiffCS는 능력 차이와 경기력을 파악하는 데 도움이 되며, GPM과 XPM은 경제적인 성과와 경험치 획득 속도를 평가하는 지표이므로 모두 승패와 연관이 있다.  그리고 승패를 예측하는 것이기 때문에, 경기 데이터를 기준으로 데이터 속성별 정규화(normalize)를 수행했다.

## 2.4 데이터 프레임 설계 

탐색적 데이터 분석과 데이터 전처리를 통해 다음과 같은 데이터 프레임을 만들고자 한다.

<table>
  <tr align="center"><th rowspan="2">Id</th><th rowspan="2">팀</th><th rowspan="2">주요지표</th><th colspan="5">포지션</th></tr>
  <tr align="center"><th>TOP</th><th>MID</th><th>JUG</th><th>ADC</th><th>SPT</th></tr>
  <tr align="center"><td rowspan="13">고유번호</td><td rowspan="13">100/200</td><td>kda</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>dealt</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>dpm</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>dpg</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>dpd</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>dtpm</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>goldearned</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>kills</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>object</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>diffdpg</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>diffcs</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>gpm</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
  <tr align="center"><td>xpm</td><td>···</td><td>···</td><td>···</td><td>···</td><td>···</td></tr>
</table>




# 3. 승패예측 모델 

## 3.1 모델 개요

각 팀의 특징 데이터를 합산하고 정규화한 후, 승패를 예측하는 **단순한 합산을 사용하는 모델**을 사용해봤다.</br> 

또한 정규화한 pkl 파일에서 특징 데이터를 추출하여 float 형식으로 변환하고, 이를 활용하여 블루팀과 레드팀의 승패를 예측해서 이 결과를 리스트에 저장하고 pkl 파일로 저장했다. 
이 pkl 파일을 csv로 변환한 후, 8:2 비율로 train, validation 데이터셋으로 분할하여 **CNN**을 사용했다.

## 3.2 성능

<table>
  <tr align="center">
    <th> </th><th> </th><th>정확도(단순)</th><th>정확도(CNN)</th></tr>
  <tr align="center"><td rowspan="2">0825</td><td>플래티넘↑</td><td>95.8%</td><td>97.6%</td></tr>
  <tr align="center">
    <td>전체</td><td>95%</td><td>95.3%</td></tr>
  <tr align="center"><td rowspan="2">0915</td><td>플래티넘↑</td><td>	94.9%</td><td>	97.4%</td></tr>
  <tr align="center">
    <td>전체</td><td>	93.4%</td><td>95.1%</td></tr>
   <tr align="center"><td rowspan="2">0917</td><td>플래티넘↑</td><td>	93.5%</td><td>94.6%</td></tr>
  <tr align="center">
    <td>전체</td><td>	92%</td><td></td></tr>
</table>

0825, 0915, 0917 각 날짜별 플래티넘 이상의 데이터와 전체 데이터의 승패예측 모델 정확도이다.</br>
CNN을 사용한 모델은 단순 합산 모델보다 모두 높은 정확도를 보이며, 플래티넘 이상의 데이터보다 전체 데이터는 약간 하락하는 경향을 보이지만 모두 정확도가 94% 이상으로, 이는 승패예측을 고려해 특징 데이터를 활용한 CNN 모델의 성능이 좋은 것을 알 수 있다. </br> 

다만 0917 플래티넘 이상의 데이터는 Overfitting 현상이 발생했다. 학습 데이터의 정확도는 98.3% , 검증 데이터의 정확도는 94.6%로 큰 차이를 보인다. 0917 플래티넘의 학습 데이터 양이 적어 발생한 문제로 예상된다. 


## 3.3 소결 

이 프로젝트에서 개발된 모델은 리그 오브 레전드 게임에서의 중요한 데이터 속성을 기반으로 팀의 승패 예측을 한다.
주어진 게임 속성을 학습하여 팀의 전반적인 활약을 예측함으로써 어떤 특정 상황에서 팀이 강하거나 약한 지에 대한 통찰력을 제공하며, 
이는 게이머들이 전략 수립에 큰 도움을 줄 수 있다. 또한 e-sports 산업에서는 경기 결과를 사전에 예측하여 투자 및 전략을 세우는 데 도움이 될 수 있다. 

이 프로젝트에서는 승패를 예측하는 주요 데이터 속성을 식별하여 총 13개를 추출하고 이를 기반으로 승패를 예측해보았다. 이를 통해 게임의 특성과 전략을 더 깊이 이해하는 것이 중요한 역할을 하는 것을 알 수 있다. 
종합적인 성과 데이터 항목인 Kda, Dealt, DPD, DTPM, kills, object, XPM 은 플레이어 및 팀의 전반적인 활약도를 평가하고 DiffDPG, Diffcs 는 팀 간의 능력 및 경제적인 격차를 나타내어 경기의 강약을 분석하는데 큰 이점을 주며,
DPG, DPM, GPM 은 어떤 플레이어나 팀이 높은 성과를 내는지를 평가하여 경기 전략의 효율성을 분석하고, goldearner와 GPM은 경기 내에 경제적으로 우위를 점하는 플레이어나 팀은 전투에 유리한 위치에 있을 가능성이 높다.
특히 kills, Object, goldearned, GPM은 상관 관계가 있는 데이터 속성들로, 초기에 적을 처치하였는지와 오브젝트를 활용하여 골드를 빠르게 획득하는 것이 이점을 얻는데 도움된다. 이로써 승패 예측에 관련이 있는 데이터 속성을 추출하여 딥러닝 모델인 CNN을 사용하면 팀의 승패를 보다 정확하게 예측하는 것을 알 수 있다. 



# 4. 결론 및 배운점

롤 승패 예측 모델의 플래티넘 이상 데이터 예측 정확도는 94.6% 에서 97.6% 가 나왔고, 전체 데이터 예측 정확도는 92% 에서 95.3%가 나왔다. 따라서 단순 합산보다 CNN 을 사용한 승패 예측 모델이 더욱 좋은 성능을 보여준다는 것을 알 수 있으며, 단순 합산 모델의 학습 시간은 약 96시간이 소요되었고, CNN 모델은 약 48시간이 소요되었다. 즉 **정확도 면에서나 학습 속도 면에서도 CNN 모델을 사용하는 것이 좋다는 것**을 알 수 있었다. 또한 승패를 예측하는데 관련이 있는 데이터 속성과, 상관관계가 있는 데이터 속성을 묶어 추출하는 것이 승패 예측 정확도를 올리는 것에 매우 중요하다는 것을 배울 수 있었으며, 롤 게임의 전반적인 지식과 바탕을 많이 알아야만 데이터를 보는 시각이 넓어지기 때문에 해보지 않았던 롤에 대해서 많이 공부할 수 있었다.
이 모델을 더 향상시키기 위해 개선한다면 object 데이터 속성을 빼고 baron, dragon 의 속성을 추출하여 학습시킬 것이다. 이유는 object 데이터는 오브젝트 개수가 합쳐져 있어 정확히 드래곤인지 바론인지 표기가 안 되어있으며, 전반전에서의 드래곤 처치는 크게 승패 예측에 중요하지 않기 때문에 정확하게 확인할 수 있는 baron, dragon 데이터를 넣는다면 모델의 정확도가 더욱 향상될 것 같다.  이 프로젝트에서 사용된 데이터 속성은 대부분 게임 전반적인 활약도와 초기 이점, 팀의 격차와 관련된 데이터 속성들을 넣었기 때문에 오브젝트와 맵 장악력, 교전에 관련된 데이터가 부족하였다고 생각되며 이를 보완한다면 예측 성능이 더욱 좋아지지 않았을까 한다. 마지막으로, 0917 플래티넘 데이터의 Overfitting 현상을 막으려면 학습률 조정,드롭아웃, 데이터 증량 등의 시도를 해볼 수 있을 것 같다. 


--------------------------------------------------
#### 코드 및 개발환경

 - <a href="https://github.com/yeon0306/LOL_project/tree/main/Code1">[코드]</a> <a href="https://github.com/yeon0306/LOL_project/blob/main/requirements.txt">[개발환경]</a> 

