# network-socket-task
[NETWORK] KAU 컴퓨터 네트워크를 수강하며 진행한 소켓 통신 과제 레포


## 목차

1. 포트포워딩 환경 세팅
2. UDP 통신 와이어샤크 분석
3. TCP 통신 와이어샤크 분석
4. 동일 컴퓨터에서 캡쳐 불가능한 이유
5. 요약 및 느낀점

<p><br/></p>


## 1. 포트포워딩 환경 세팅

프로젝트에서 Server 역할을 맡았으므로, Client 역할을 맡은 팀원이 나의 환경으로 접속할 수 있도록 세팅한다.

<img src="https://github.com/cobinding/network-socket-task/assets/102461290/d4e15c25-95af-425b-8b39-f156e6bec0b2.png" width="850" height="300">

- **내부 IP:** 공유기가 내 컴퓨터에 할당한 IP 주소로, MacOS는 wifi 설정에서 확인 가능하다.
- **포트:** 패킷 분석을 위해 다른 포트들과 겹치지 않도록 12000으로 설정한다.

이 포트 값과 공인 IP를 통해 Client 역할자가 나에게 통신을 요청 및 커넥션할 수 있게 된다. (방화벽 허용 시에)

<p><br/></p>

## 2. UDP 통신 와이어샤크 분석

![image](https://github.com/cobinding/network-socket-task/assets/102461290/b5c2a571-e200-4690-8b6c-814580174cca)
*서버 측에서 요청 처리 로직을 확인하기 위해 print로 디버깅하였습니다.
<p><br/></p>

![image](https://github.com/cobinding/network-socket-task/assets/102461290/cda7368a-8088-404c-8943-28f6e33797ca)

port 12000으로 필터링

위 결과에 대해 와이어샤크로 패킷을 캡쳐해보면, 클라이언트 측 `175.213.35.145`이 서버측 `192.168.45.195`와 통신하는 것을 알 수 있다.

<p><br/></p>

![image](https://github.com/cobinding/network-socket-task/assets/102461290/b5d89769-bd8d-46a3-baa2-f5e804360270)

- 하나를 선택해서 상세 내용을 살펴보면, 클라이언트의 port는 50662로 확인된다.
- 16비트로 표현된 **CheckSum**을 확인할 수 있다. 이를 통해 패킷이 전송과정 중에 손상되지 않고 잘 전달되었음을 확인할 수 있다.

<p><br/></p>

![image](https://github.com/cobinding/network-socket-task/assets/102461290/f0d90ee7-bdfb-490f-a9cf-fbd9974078cd)

- 두 번째 패킷 상세 내용을 보면 **Stream index**가 21로, 첫 번째의 패킷 상세 내용과 같음을 알 수 있다. 이 내용은 하나의 통신에 대한 내부 와이어샤크 매핑으로 소문자로 적힌 문자열을 보내고 → 다시 그 문자열을 UpperCase로 반환하는 하나의 통신이 같은 index를 갖는 것을 확인할 수 있다.

<p><br/></p>

<img src="https://github.com/cobinding/network-socket-task/assets/102461290/01b64bab-40bd-4c79-9804-953f3848406a.png" weight="400" height="200">
<p>클라이언트 담당자의 화면에서 서버 측에서의 반환이 잘되었음을 확인하였다.</p>
