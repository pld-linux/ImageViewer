Summary:	Simple image viewer for GNUstep
Summary(pl):	Prosta przegl±darka obrazków dla ¶rodowiska GNUstep
Name:		ImageViewer
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnustep.org/pub/gnustep/usr-apps/%{name}-%{version}.tar.gz
# Source0-md5:	4d1cfe134814c51a4c7b639bec19d8f8
URL:		http://www.nice.ch/~phip/softcorner.html#img
BuildRequires:	gnustep-extensions-devel
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
This is ImageViewer, a simple image viewer application for GNUstep.

%description -l pl
To jest ImageViewer - prosta przegl±darka obrazków dla ¶rodowiska
GNUstep.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_prefix}/System/Applications/ImageViewer.app
%attr(755,root,root) %{_prefix}/System/Applications/ImageViewer.app/ImageViewer
%dir %{_prefix}/System/Applications/ImageViewer.app/Resources
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.desktop
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.plist
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}/ImageViewer
%{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
