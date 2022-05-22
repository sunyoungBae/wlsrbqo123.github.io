# 정의
실행 컨텍스트를 생성할 때 VariableEnvironment에 정보를 먼저 담은 다음, 이를 그대로 복사해서 LexicalEnvironment를 만들고, 이후에는 LexicalEnvironment를 주로 활용합니다.

# 구성
- environmentRecord
- outerEnvironmentReference

초기화시 LexicalEnvironment와 동일하고 이 후 코드 진행에 따라서 서로 달라지게 될 것이므로 자세한 내용은 LexicalEnvironment를 통해 알아봅니다.
