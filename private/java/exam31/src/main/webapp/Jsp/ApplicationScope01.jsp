<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
try {
	//ServletContext application = getServletContext();
	//jsp는 이미 application 내장 객체를 갖고있기 때문에 호출 불필요.
	int value = (int)application.getAttribute("value");
	value+=2;
	application.setAttribute("value", value);
%>
	<h1>value : <%=value%></h1>
<%
} catch (NullPointerException e) {
%>
	<h1>value의 값이 설정되지 않았습니다.</h1>
<% 
}
%>
</body>
</html>