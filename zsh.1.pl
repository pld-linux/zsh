.\" {PTM/MK/0.1/20-07-1999/"Pow³oka Z"}
.\" Translation 1999 Micha³ Kuratczyk <kura@pld.org.pl>
.TH "ZSH" "1" "Pa¼dziernik 29, 1998" "zsh 3.1.5"
.SH NAZWA
zsh \- Pow³oka Z
.SH STRESZCZENIE
Poniewa¿ zsh posiada wiele cech, podrêcznik ten zosta³ podzielony na
nastêpuj±ce sekcje:
.PP
.PD 0
.TP
\fIzsh\fP(1)		Rzut oka na zsh (ta sekcja)
.TP
\fIzshmisc\fP(1)	To co nie zmie¶ci³o siê w innych sekcjach
.TP
\fIzshexpn\fP(1)	Rozwijanie poleceñ i parametrów zsh
.TP
\fIzshparam\fP(1)	Parametry zsh
.TP
\fIzshoptions\fP(1)	Opcje zsh
.TP
\fIzshbuiltins\fP(1)	Wbudowane funkcje zsh
.TP
\fIzshzle\fP(1)		Edycja wiersza poleceñ zsh
.TP
\fIzshcompctl\fP(1)	Kontrola automatycznego dope³niania
.TP
\fIzshmodules\fP(1)	£adowalne modu³y zsh
.TP
\fIzshall\fP(1)		Wszystkie sekcje razem
.PD
.SH OPIS
.'
Zsh jest UNIXowym interpretatorem poleceñ (pow³ok±, shell'em) nadaj±cym siê
zarówno do interaktywnej pracy z systemem jak i do wykonywania skryptów.
Z po¶ród standardowych pow³ok zsh najbardziej przypomina \fBksh\fP(1), ale
zawiera wiele ulepszeñ.  Zsh posiada edycjê wiersza poleceñ, wbudowan±
korekcjê pisowni, programowalne dope³nianie poleceñ, funkcje (z automatycznym
³adowaniem), historiê poleceñ i mnóstwo innych cech.
.SH AUTOR
Pierwotnie zsh zosta³ napisany przez Paula Falstada \fB<pf@zsh.org>\fP.
Obecnie zsh jest utrzymywany przez cz³onków listy dyskusyjnej zsh-workers
\fB<zsh-workers@math.gatech.edu>\fP. Koordynatorem projektu jest obecnie 
Andrew Main (Zefram) \fB<zefram@zsh.org>\fP. Z koordynatorem mo¿na siê
skontaktowaæ pisz±c na adres \fB<coordinator@zsh.org>\fP, ale sprawy
dotycz±ce kodu powinny byæ kierowane na listê dyskusyjn±.
.'
.SH DOSTÊPNO¦Æ
.'
Zsh jest dostêpny z nastêpuj±cych anonimowych serwerów FTP.  Mirrory te s±
czêsto aktualizowane. Serwery oznaczone przez \fI(G)\fP mog± byæ aktualizowane
wzglêdem \fBftp.math.gatech.edu\fP zamiast wzglêdem serwera g³ównego. Serwery
oznaczone przez \fI(H)\fP mog± byæ aktualizowane wzglêdem \fBftp.cs.elte.hu\fP.
.PP
.PD 0
.TP
.PD
Serwery g³ówne
.nf
\fBftp://ftp.zsh.org/pub/zsh/\fP
\fBhttp://www.zsh.org/pub/zsh/\fP
.fi
.TP
Australia
.nf
\fBftp://ftp.zsh.org/pub/zsh/\fP
\fBhttp://www.zsh.org/pub/zsh/\fP
\fBftp://ftp.ips.oz.au/pub/packages/zsh/\fP  \fI(G)\fP  \fI(H)\fP
.fi
.TP
Dania
.nf
\fBftp://sunsite.auc.dk/pub/unix/shells/zsh/\fP
.fi
.TP
Finlandia
.nf
\fBftp://ftp.funet.fi/pub/unix/shells/zsh/\fP  \fI(H)\fP
.fi
.TP
Francja
.nf
\fBftp://ftp.cenatls.cena.dgac.fr/pub/shells/zsh/\fP
.fi
.TP
Niemcy
.nf
\fBftp://ftp.fu\-berlin.de/pub/unix/shells/zsh/\fP  \fI(H)\fP
\fBftp://ftp.gmd.de/packages/zsh/\fP  \fI(H)\fP
\fBftp://ftp.uni\-trier.de/pub/unix/shell/zsh/\fP  \fI(H)\fP
.fi
.TP
Wêgry
.nf
\fBftp://ftp.cs.elte.hu/pub/zsh/\fP
\fBhttp://www.cs.elte.hu/pub/zsh/\fP
\fBftp://ftp.kfki.hu/pub/packages/zsh/\fP  \fI(H)\fP
.fi
.TP
Izrael
.nf
\fBftp://ftp.math.technion.ac.il/mirror/ftp.zsh.org/pub/zsh/\fP
\fBhttp://www.math.technion.ac.il/mirror/ftp.zsh.org/pub/zsh/\fP
.fi
.TP
Japonia
.nf
\fBftp://ftp.tohoku.ac.jp/mirror/zsh/\fP  \fI(H)\fP
\fBftp://ftp.nis.co.jp/pub/shells/zsh/\fP  \fI(H)\fP
.fi
.TP
Norwegia
.nf
\fBftp://ftp.uit.no/pub/unix/shells/zsh/\fP  \fI(H)\fP
.fi
.TP
Rumunia
.nf
\fBftp://ftp.roedu.net/pub/mirrors/ftp.zsh.org/pub/zsh/\fP
.fi
.TP
S³owenia
.nf
\fBftp://ftp.siol.net/pub/unix/shells/zsh/\fP  \fI(H)\fP
.fi
.TP
Szwecja
.nf
\fBftp://ftp.lysator.liu.se/pub/unix/zsh/\fP  \fI(H)\fP
.fi
.TP
Wielka Brytania
.nf
\fBftp://ftp.net.lut.ac.uk/zsh/\fP  \fI(H)\fP
\fBftp://sunsite.doc.ic.ac.uk/packages/unix/shells/zsh/\fP  \fI(G)\fP
.fi
.TP
USA
.nf
\fBftp://ftp.math.gatech.edu/pub/zsh/\fP
\fBftp://uiarchive.uiuc.edu/pub/packages/shells/zsh/\fP
\fBftp://ftp.sterling.com/zsh/\fP  \fI(G)\fP  \fI(H)\fP
\fBftp://ftp.rge.com/pub/shells/zsh/\fP  \fI(G)\fP  \fI(H)\fP
\fBftp://foad.org/pub/zsh/\fP
\fBhttp://foad.org/zsh/\fP
.fi
.SH Listy dyskusyjne
Istniej± trzy listy dyskusyjne po¶wiêcone zsh:
.PP
.PD 0
.TP
.PD
\fB<zsh-announce@math.gatech.edu>\fP
Informacje o nowych wersjach, wiêkszych zmianach oraz comiesiêcznym FAQ,
czyli odpowiedziami na najczê¶ciej zadawane pytania. (lista moderowana)
.TP
\fB<zsh-users@math.gatech.edu>\fP
Dyskusje u¿ytkowników.
.TP
\fB<zsh-workers@math.gatech.edu>\fP
Rozwój, raporty o b³êdach i ³aty na nie.
.PP
¯eby zapisaæ siê na listê wy¶lij list z polem SUBJECT `\fBsubscribe\fP
\fI<adres-e-mail>\fP'
na adres administracyjny zwi±zany z odpowiedni± grup±.
.PP
.PD 0
.TP
\fB<zsh-announce-request@math.gatech.edu>\fP
.TP
\fB<zsh-users-request@math.gatech.edu>\fP
.TP
\fB<zsh-workers-request@math.gatech.edu>\fP
.PD
.PP
Wypisywanie siê z listy jest analogiczne.
.PP
WYSTARCZY ZAPISAÆ SIÊ NA JEDN¡ LISTÊ.
Wszystkie listy z \fBzsh-announce\fP s± automatycznie przesy³ane na listê
\fBzsh-users\fP, za¶ wszystkie listy z \fBzsh-users\fP s± automatycznie
przesy³ane na \fBzsh-workers\fP.
.PP
Masz problemy z zapisaniem lub wypisaniem siê na któr±¶ z list, informacjê o
tym wy¶lij na adres \fB<listmaster@zsh.org>\fP. Listy dyskusyjne s±
utrzymywane przez Richarda Colemana \fB<coleman@zsh.org>\fP.
.PP
Listy s± archiwizowane; archiwum mo¿na dostaæ wysy³aj±c list na 
podany adres administracyjny listy. Istnieje równie¿ hipertekstowa wersja
archiwum utrzymywana przez Geoffa Winga \fB<gcw@zsh.org>\fP i dostêpna
pod adresem \fBhttp://www.zsh.org/mla/\fP.
.SH ZSH FAQ
Zsh posiada listê najczê¶ciej zadawanych pytañ (FAQ), utzrymywane przez
Petera Stephensona \fB<pws@zsh.org>\fP.  Jest ona regularnie wysy³ana na
grupê dyskusyjn± \fBcomp.unix.shell\fP oraz listê  \fBzsh-announce\fP.
Najnowsz± wersjê mo¿na znale¼æ na dowolnym z wymienionych serwerów FTP lub
pod adresem \fBhttp://www.zsh.org/FAQ/\fP. Adres kontaktowy do spraw
zwi±zanych z FAQ to \fB<faqmaster@zsh.org>\fP.
.SH Strona WWW ZSH
Zsh posiada stronê WWW pod adresem \fBhttp://www.zsh.org/\fP. Jest ona
utrzymywana przez Karstena Thygesena \fB<karthy@zsh.org>\fP z SunSITE Dania.
Adres kontaktowy do spraw zwi±zanych z witryn± WWW to \fB<webmaster@zsh.org>\fP.
.SH PARAMETRY STARTOWE
Je¿eli flaga \fB\-s\fP nie zosta³a podana, a zosta³ podany jaki¶ argument to
pierwszy argument uznawany jest za ¶cie¿kê skryptu, który ma zostaæ wykonany.
Pozosta³e argumenty s± traktowane jako parametry pozycyjne. Nastêpuj±ce flagi
s± interpretowane przez zsh przy starcie:
.PP
.PD 0
.TP
.PD
\fB\-c\fP \fIci±g poleceñ\fP
Wykonaj \fIci±g poleceñ\fP.
.'
.TP
\fB\-i\fP
Wymu¶ na pow³oce interaktywno¶æ.
.'
.TP
\fB\-s\fP
Wczytuj polecenia ze standardowego wej¶cia.
.SH PLIKI STARTOWE/KOÑCOWE
Polecenia s± najpierw czytane z \fB/etc/zshenv\fP. Je¿eli opcja \fBRCS\fP
nie jest ustawiona w \fB/etc/zshenv\fP, wszystkie pozosta³e pliki startowe s±
pomijane. W przeciwnym wypadku polecenia s± czytane z \fB$ZDOTDIR/.zshenv\fP.
Je¿eli pow³oka jest pow³ok± zameldowania (loginow±), polecenia s± czytane
z \fB/etc/zprofile\fP, a nastêpnie z \fB$ZDOTDIR/.zprofile\fP. Nastêpnie,
je¿eli pow³oka jest interaktywna, polecenia s± czytane z \fB/etc/zshrc\fP
i \fB$ZDOTDIR/.zshrc\fP. Na koniec, je¿eli pow³oka jest pow³ok± zameldowania,
czytane s± pliki \fB/etc/zlogin\fP i \fB$ZDOTDIR/.zlogin\fP.
.PP
Je¿eli zmienna \fB$ZDOTDIR\fP nie jest ustawiona, u¿ywana jest zmienna
\fB$HOME\fP. Wymienione powy¿ej pliki z katalogu \fB/etc\fP, w zale¿no¶ci od
systemu, mog± znajdowaæ siê w innym katalogu.
.SH PLIKI
.PD 0
.TP
\fB$ZDOTDIR/.zshenv\fP
.TP
\fB$ZDOTDIR/.zprofile\fP
.TP
\fB$ZDOTDIR/.zshrc\fP
.TP
\fB$ZDOTDIR/.zlogin\fP
.TP
\fB$ZDOTDIR/.zlogout\fP
.TP
\fB${TMPPREFIX}*\fP   (domy¶lnie /tmp/zsh*)
.TP
\fB/etc/zshenv\fP
.TP
\fB/etc/zprofile\fP
.TP
\fB/etc/zshrc\fP
.TP
\fB/etc/zlogin\fP
.TP
\fB/etc/zlogout\fP   (katalog \fB/etc\fP jest domy¶lny, ale pliki te mog± znajdowaæ siê w innym katalogu)
.PD
.SH ZOBACZ TAK¯E
\fIsh\fP(1),
\fIcsh\fP(1),
\fItcsh\fP(1),
\fIrc\fP(1),
\fIbash\fP(1),
\fIksh\fP(1),
\fIzshbuiltins\fP(1),
\fIzshcompctl\fP(1),
\fIzshexpn\fP(1),
\fIzshmisc\fP(1),
\fIzshmodules\fP(1),
\fIzshoptions\fP(1),
\fIzshparam\fP(1),
\fIzshzle\fP(1)
.PP
\fBIEEE Standard for information Technology - Portable
Operating System Interface (POSIX) - Part 2:
Shell and Utilities\fP, IEEE Inc, 1993, ISBN 1\-55937\-255\-9.
