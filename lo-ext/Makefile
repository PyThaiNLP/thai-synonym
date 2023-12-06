top_srcdir=..

# Commands
GEN_THES = python3 $(top_srcdir)/utils/gen-thesaurus.py
GEN_IDX = /usr/share/mythes/th_gen_idx.pl  # From package "libmythes-dev"
ZIP = zip  # From package "zip"

# DATA FILES
CSV_SRC = $(top_srcdir)/data.csv
DAT_FILE = thai-thesaurus/th_th_TH_v2.dat
IDX_FILE = thai-thesaurus/th_th_TH_v2.idx
OXT_FILE = thai-thesaurus.oxt

CLEANFILES = $(DAT_FILE) $(IDX_FILE)
DISTCLEANFILES = $(OXT_FILE)

all: $(OXT_FILE)

clean:
	rm -f $(CLEANFILES)

distclean: clean
	rm -f $(DISTCLEANFILES)

$(DAT_FILE): $(CSV_SRC)
	$(GEN_THES) $< $@

$(IDX_FILE): $(DAT_FILE)
	$(GEN_IDX) -o $@ < $<

$(OXT_FILE): $(DAT_FILE) $(IDX_FILE)
	rm -f $(OXT_FILE)
	(cd thai-thesaurus; $(ZIP) -r ../$(OXT_FILE) *)
