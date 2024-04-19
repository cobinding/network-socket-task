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

<p><br/></p>
<p><br/></p>

## 3. TCP 통신 와이어샤크 분석

![image](https://github.com/cobinding/network-socket-task/assets/102461290/2416715b-954e-4779-aaca-bb2ee15adf6e)
![image](https://github.com/cobinding/network-socket-task/assets/102461290/4f376e5c-178a-4e30-b5cc-9b95f87e43c8)

TCP는 UDP와 달리 segment numbering, 3 way handshake 등을 통해 **신뢰성을 보장하는 통신**을 한다. 따라서 wireshark를 통해 캡쳐했을 때 위와 같이 복잡한 통신 과정을 보인다.

<p><br/></p>

### Wireshark를 통해 알아본 3way handshake 과정

1. SYN

![image](https://github.com/cobinding/network-socket-task/assets/102461290/8c56a461-c614-4ff7-89fa-f7325d5bc634)

SYN - Sequence Number가 2917077022로 상대값은 0이다. 즉, 첫 번째 TCP 통신으로, 서버는 이에 대한 SYN, ACK를 반환해야 한다. 이를 다음 패킷의 상세내용을 통해 확인할 수 있다.

1. SYN, ACK

![image](https://github.com/cobinding/network-socket-task/assets/102461290/e44d8ab8-24c7-405f-ab71-d70cc230982f)

- Acknoweldgement number를 보면 2917077023으로, 클라이언트에게 확인했다는 신호를 준다. 

1. ACK

![image](https://github.com/cobinding/network-socket-task/assets/102461290/3afe5ae8-e3fd-4490-9ffa-b5634edad478)


- sequence number 1증가, Acknowledgment number로 확인 전달

이를 통해 서로 3way를 문제없이 잘 하고있음을 wireshark를 통해 확인하였다.

<p><br/></p>

## 4. 동일 PC wireshack capture

Windows 네트워킹은 같은 소스 및 대상 주소를 가진 루프백 어댑터가 없고, 트래픽이 드라이버 스택에 도달하지 않으므로 Windows 운영체제 환경에서 와이어샤크가 패킷을 가로챌 때 제대로 기록되지 않기 때문이다.

<p><br/></p>

## 5. 요약 및 느낀점

wireshark를 통해 UDP와 TCP의 차이점을 확실히 알 수 있었고, TCP 통신의 부하에 대해서도 고민하게 되었다.
