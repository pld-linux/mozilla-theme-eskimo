Summary:	Feel the chill of a sunny winter morning!
Summary(pl):	Poczuj ch��d s�onecznego zimowego poranka!
Name:		mozilla-theme-eskimo
Version:	1.0.1
%define		_realname	eskimo
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east1.mozdev.org/themes/%{_realname}1RC3.jar
# Source0-md5:	47aefbdef7ea393f0635587b497756b4
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/eskimo.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Feel the chill of a sunny winter morning!

%description -l pl
Poczuj ch��d s�onecznego zimowego poranka!

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
