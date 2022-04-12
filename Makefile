default:
	# <- indented by tab. (try use spaces!)
	-cat doing # `-`: ignore error and continue
	rm -f doing
	tail timetrack

%:
	sh time.sh $@
