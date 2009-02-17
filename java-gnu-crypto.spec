%bcond_without	javadoc			# don't build javadoc

%define		srcname		gnu-crypto

Summary:	Cryptographic primitives and tools in the Java
Summary(pl.UTF-8):	Narzędzia i biblioteki kryptograficzne dla Javy
Name:		java-gnu-crypto
Version:	2.0.1
Release:	1
License:	GPL v2
Group:		Libraries/Java
Source0:	http://ftp.gnu.org/gnu/gnu-crypto/binaries/gnu-crypto-%{version}-bin-r1.tar.bz2
# Source0-md5:	278fdddbbad9a26344c6fc24206edf2f
URL:		http://www.gnu.org/software/gnu-crypto/
BuildRequires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Crypto, part of the GNU project, released under the aegis of GNU,
aims at providing free, versatile, high-quality, and provably correct
implementations of cryptographic primitives and tools in the Java
programming language for use by programmers and end-users.

%package javadoc
Summary:	API documentation for GNU Crypto
Summary(pl.UTF-8):	Dokumentacja API GNUrypto
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
API documentation for GNU Crypto.

%description javadoc -l pl.UTF-8
Dokumentacja API GNU Crypto.

%prep
%setup -q -n %{srcname}-%{version}-bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{srcname}-%{version}}
install lib/gnu-crypto.jar $RPM_BUILD_ROOT/%{_javadir}/gnu-crypto-%{version}.jar
install lib/javax-crypto.jar $RPM_BUILD_ROOT/%{_javadir}/javax-crypto-%{version}.jar
install lib/javax-security.jar $RPM_BUILD_ROOT/%{_javadir}/javax-security-%{version}.jar
ln -s gnu-crypto-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/gnu-crypto.jar
ln -s javax-crypto-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/javax-crypto.jar
ln -s javax-security-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/javax-security.jar

# javadoc
%if %{with javadoc}
cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUILD THANKS
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
