from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import MDSplus as mds
import os, time, glob

def compute(shotnum, a):
	con = mds.Connection('lithos.pppl.gov:8000::')
	t = con.openTree('ltx', shotnum)
	data = t.get(a).data
	timescale = t.getNode(a).dim_of().data()
	plt.figure()
	plt.plot(timescale, dat.record.data())
	plt.title('B=%g' % (B))

	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
	# Remove old plot files
		for filename in glob.glob(os.path.join('static', '*.png')):
			os.remove(filename)
	# Use time since Jan 1, 1970 in filename in order make
	# a unique filename that the browser has not chached
	plotfile = os.path.join('static', str(time.time()) + '.png')
	plt.savefig(plotfile)
	return plotfile

#if __name__ == '__main__':
#print (compute(1, 0.1, 1, 20))