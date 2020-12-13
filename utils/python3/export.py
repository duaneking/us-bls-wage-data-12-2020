import uuid
import os
import psycopg2

db_host = 'sql server hostname here'
db_name = 'bls2020wagedata'
user_name = 'postgres'
user_passwd = ''


# Get all records for a query.
def query(conn, query):
	cur = conn.cursor()

	if not cur:
		raise Exception('No DB Cursor.  Check your system.')

	with cur:
		cur.execute(query)
		
		return cur.fetchall()


# Could be solved with a CSV parser,  but I want to keep dependencies small here.
# This works now.
def format(field):
	if field is None:
		return 'NOPE'  # The US BLS has intentionally hidden this data from the public.  We do not have it.
	
	fieldString = str(field)
	
	return '"{}"'.format(fieldString) if "," in fieldString else fieldString
	
	

def save(results, filename):
	# Simple CSV Header.
	header = "soccode, level1, level2, level3, level4, fullcode, title, description"
	
	with open(filename, "a") as file:
		file.write(header + '\n')
		
		for line in results:
			formated_entries = [format(field) for field in line]

			result = ','.join(formated_entries) + '\n'
			
			file.write(result)


# The US BLS intentionally neutered this data dump.
# This geographical data does not reflect GIS standards and can not be used to reconstruct a map UI without excessive work.
# This seems intentional.  You have been warned.
def export_data(db_host, db_name, user_name, user_passwd):
	conn = psycopg2.connect(
		host=db_host,
		port=5432,
		dbname=db_name,
		user=user_name,
		password=user_passwd)

	try:

		if not conn:
			raise Exception('No DB Connection.  Check your ENV Values.')

		with conn:
			geos = query(conn, "SELECT area, areaname, stateab, countytownname FROM geography")
			
			for geo in geos:
				# for every geo, export common data for that area.
				area = geo[0]
				areaname = geo[1]
				stateab = geo[2]
				countytownname = geo[3]
				
				sql = "select a.soccode, a.level1, a.level2, a.level3, a.level4, o.onetcode, o.onettitle, o.onetdescription from alc_export as a, xwalk_plus as x, onet_occs as o where a.area = '" + str(area) + "' and a.soccode = x.oes_soccode and o.onetcode = x.onetcode"
				
				records = query(conn, sql)
				
				# This is not a reusable tool and it is not meant to be reused unless somebody really wants to duplicate the output I generated.
				file = str(stateab) + "_" + str(countytownname).replace(' ', '_').replace('/', '_') + '_' + str(areaname).replace('/', '_').replace(',', '_').replace(' ', '_').replace(stateab, '').replace('__', '_').replace('__', '_').replace('_.', '') + ".csv"
				file = file.replace('_.csv', '.csv')
				
				# Debugging.
				if os.path.exists( file ):
					print( "duplicated file: " + file )
					file = file.replace('.csv', '_' + uuid.uuid4().hex + '.csv')
					print( "duplicated file: " + file )
					
				print("Saving: " + file)
				
				save(records, file)
				
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()



if __name__ == '__main__':
	export_data(db_host, db_name, user_name, user_passwd)

