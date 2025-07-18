Summary:	Shows status of logical drives attached to HP SmartArray controllers
Summary(pl.UTF-8):	Wyświetla status logicznych dysków stworzonych w kontrolerach HP SmartArray
Name:		cciss_vol_status
Version:	1.12
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/cciss/%{name}-%{version}.tar.gz
# Source0-md5:	83cbd9907efeff48eb30e2a3ca89faa5
Patch0:		new-ids.patch
URL:		http://cciss.sourceforge.net/#cciss_utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cciss_vol_status is a very lightweight program to report the status of
logical drives on Smart Array controllers and also fibre channel
attached MSA1000.

%description -l pl.UTF-8
cciss_vol_status to lekki program do raporotwania statusu logicznych
dysków kontrolera Smart Array jak również MSA1000.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--bindir=%{_sbindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/cciss_vol_status
%{_mandir}/man8/cciss_vol_status*
