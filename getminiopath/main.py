import os
import subprocess
from ruamel import yaml
import time

start_time = time.time() # 开始时间

def popen_communicate_sys_cmd(cmd):
    proc = subprocess.Popen([cmd],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdoutdata, stderrdata = proc.communicate()
    ret = proc.returncode
    if ret == 0:
        ret = [True, stdoutdata.decode('utf-8'), proc.pid, cmd]
    else:
        ret = [False, stderrdata.decode('utf-8'), proc.pid, cmd]
    return ret

mercury_ids_txt = "./mercury_ids.txt"

txt_fh = open(mercury_ids_txt)
lines_list = txt_fh.readlines()
lines_minio_list = []
count = len(lines_list)
success = 0
fail = 0
txt_fh.close()
for i in range(len(lines_list)):
    output_object_prefix = ''
    line = lines_list[i].replace('\n', '')
    req = '10.219.41.11:98081/task-engine/v1/tasks/{0}'.format(line)
    cmd = "curl --location {0}".format(req)

    ret = popen_communicate_sys_cmd(cmd)
    if ret[0]:
        yaml_data = ret[1]
        config_dict = yaml.load(yaml_data, Loader=yaml.RoundTripLoader)
        if config_dict == None or len(config_dict) == 0:
            fail = fail + 1
            break
        else:
            parameters = config_dict['task']['arguments']['parameters']
            for parameter in parameters:
                for k, v in parameter.items():
                    if v == 'output_object_prefix':
                        output_object_prefix = parameter['value']
                        line_minio = "{0:40} {1}".format(line, output_object_prefix)
                        print(line_minio)
                        lines_minio_list.append(line_minio)
                        break
        
        if output_object_prefix == '':
            fail = fail + 1
        else:
            success = success + 1
            #print("{0} {1}".format(line, output_object_prefix))

    else:
        fail = fail + 1

    if i % 5 == 0:
        time.sleep(1)



with open('{0}mercury_ids_txt'.format("minio"), 'w') as output:
    for i in range(len(lines_minio_list)):
        line = lines_minio_list[i] + '\n'
        output.write(line)

print("count:{0}  success:{1} fail:{2}".format(count, success, fail))

end_time = time.time() #结束时间
print("程序耗时%f秒." % (end_time - start_time))