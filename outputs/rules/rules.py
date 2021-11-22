def findDecision(obj): #obj[0]: chieu cao, obj[1]: tay, obj[2]: chan, obj[3]: than tren, obj[4]: than duoi, obj[5]: tong the, obj[6]: linh hoat, obj[7]: suc ben, obj[8]: can bang, obj[9]: toc do
	# {"feature": "linh hoat", "instances": 456, "metric_value": 2.9382, "depth": 1}
	if obj[6] == 'tot':
		# {"feature": "tong the", "instances": 360, "metric_value": 2.9807, "depth": 2}
		if obj[5] == 'khoe':
			# {"feature": "than duoi", "instances": 296, "metric_value": 3.2365, "depth": 3}
			if obj[4] == 'khoe':
				# {"feature": "toc do", "instances": 236, "metric_value": 3.1708, "depth": 4}
				if obj[9] == 'nhanh':
					# {"feature": "than tren", "instances": 170, "metric_value": 3.2094, "depth": 5}
					if obj[3] == 'khoe':
						# {"feature": "suc ben", "instances": 112, "metric_value": 3.3074, "depth": 6}
						if obj[7] == 'tot':
							# {"feature": "chieu cao", "instances": 104, "metric_value": 3.3158, "depth": 7}
							if obj[0] == 'cao':
								# {"feature": "tay", "instances": 61, "metric_value": 3.3734, "depth": 8}
								if obj[1] == 'dai':
									# {"feature": "can bang", "instances": 36, "metric_value": 3.3921, "depth": 9}
									if obj[8] == 'tot':
										# {"feature": "chan", "instances": 21, "metric_value": 3.4399, "depth": 10}
										if obj[2] == 'dai':
											return 'Tennis'
										elif obj[2] == 'ngan':
											return 'Tennis'
										else: return 'Tennis'
									elif obj[8] == 'kem':
										# {"feature": "chan", "instances": 15, "metric_value": 2.9736, "depth": 10}
										if obj[2] == 'dai':
											return 'Tennis'
										elif obj[2] == 'ngan':
											return 'Tennis'
										else: return 'Tennis'
									else: return 'Tennis'
								elif obj[1] == 'ngan':
									# {"feature": "can bang", "instances": 25, "metric_value": 2.8839, "depth": 9}
									if obj[8] == 'tot':
										# {"feature": "chan", "instances": 15, "metric_value": 2.9736, "depth": 10}
										if obj[2] == 'ngan':
											return 'Ban cung'
										elif obj[2] == 'dai':
											return 'Ban cung'
										else: return 'Ban cung'
									elif obj[8] == 'kem':
										# {"feature": "chan", "instances": 10, "metric_value": 2.3219, "depth": 10}
										if obj[2] == 'dai':
											return 'Chay ben'
										elif obj[2] == 'ngan':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							elif obj[0] == 'thap':
								# {"feature": "can bang", "instances": 43, "metric_value": 2.7751, "depth": 8}
								if obj[8] == 'tot':
									# {"feature": "tay", "instances": 26, "metric_value": 2.8543, "depth": 9}
									if obj[1] == 'ngan':
										# {"feature": "chan", "instances": 14, "metric_value": 2.9502, "depth": 10}
										if obj[2] == 'ngan':
											return 'Ban cung'
										elif obj[2] == 'dai':
											return 'Ban cung'
										else: return 'Ban cung'
									elif obj[1] == 'dai':
										# {"feature": "chan", "instances": 12, "metric_value": 2.585, "depth": 10}
										if obj[2] == 'dai':
											return 'Ban cung'
										elif obj[2] == 'ngan':
											return 'Ban cung'
										else: return 'Ban cung'
									else: return 'Ban cung'
								elif obj[8] == 'kem':
									# {"feature": "tay", "instances": 17, "metric_value": 2.2051, "depth": 9}
									if obj[1] == 'ngan':
										# {"feature": "chan", "instances": 9, "metric_value": 2.281, "depth": 10}
										if obj[2] == 'ngan':
											return 'Chay ben'
										elif obj[2] == 'dai':
											return 'Chay ben'
										else: return 'Chay ben'
									elif obj[1] == 'dai':
										# {"feature": "chan", "instances": 8, "metric_value": 2.0, "depth": 10}
										if obj[2] == 'dai':
											return 'Chay ben'
										elif obj[2] == 'ngan':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							else: return 'Chay ben'
						elif obj[7] == 'kem':
							return 'Ban cung'
						else: return 'Ban cung'
					elif obj[3] == 'yeu':
						# {"feature": "chieu cao", "instances": 58, "metric_value": 2.3063, "depth": 6}
						if obj[0] == 'cao':
							# {"feature": "tay", "instances": 32, "metric_value": 2.375, "depth": 7}
							if obj[1] == 'dai':
								# {"feature": "chan", "instances": 20, "metric_value": 2.5219, "depth": 8}
								if obj[2] == 'dai':
									# {"feature": "can bang", "instances": 11, "metric_value": 2.5503, "depth": 9}
									if obj[8] == 'tot':
										# {"feature": "suc ben", "instances": 6, "metric_value": 2.585, "depth": 10}
										if obj[7] == 'tot':
											return 'Boi'
										else: return 'Boi'
									elif obj[8] == 'kem':
										# {"feature": "suc ben", "instances": 5, "metric_value": 2.3219, "depth": 10}
										if obj[7] == 'tot':
											return 'Boi'
										else: return 'Boi'
									else: return 'Boi'
								elif obj[2] == 'ngan':
									# {"feature": "can bang", "instances": 9, "metric_value": 2.281, "depth": 9}
									if obj[8] == 'tot':
										# {"feature": "suc ben", "instances": 5, "metric_value": 2.3219, "depth": 10}
										if obj[7] == 'tot':
											return 'Chay ben'
										else: return 'Chay ben'
									elif obj[8] == 'kem':
										# {"feature": "suc ben", "instances": 4, "metric_value": 2.0, "depth": 10}
										if obj[7] == 'tot':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							elif obj[1] == 'ngan':
								# {"feature": "chan", "instances": 12, "metric_value": 1.585, "depth": 8}
								if obj[2] == 'dai':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								elif obj[2] == 'ngan':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							else: return 'Chay ben'
						elif obj[0] == 'thap':
							# {"feature": "tay", "instances": 26, "metric_value": 1.8543, "depth": 7}
							if obj[1] == 'ngan':
								# {"feature": "chan", "instances": 14, "metric_value": 1.9502, "depth": 8}
								if obj[2] == 'ngan':
									# {"feature": "suc ben", "instances": 8, "metric_value": 2.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 8, "metric_value": 2.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								elif obj[2] == 'dai':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							elif obj[1] == 'dai':
								# {"feature": "chan", "instances": 12, "metric_value": 1.585, "depth": 8}
								if obj[2] == 'dai':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								elif obj[2] == 'ngan':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Chay ben'
										elif obj[8] == 'kem':
											return 'Chay ben'
										else: return 'Chay ben'
									else: return 'Chay ben'
								else: return 'Chay ben'
							else: return 'Chay ben'
						else: return 'Chay ben'
					else: return 'Chay ben'
				elif obj[9] == 'cham':
					# {"feature": "suc ben", "instances": 66, "metric_value": 2.0141, "depth": 5}
					if obj[7] == 'tot':
						# {"feature": "than tren", "instances": 58, "metric_value": 1.9614, "depth": 6}
						if obj[3] == 'khoe':
							# {"feature": "can bang", "instances": 38, "metric_value": 2.1427, "depth": 7}
							if obj[8] == 'tot':
								# {"feature": "tay", "instances": 28, "metric_value": 2.1645, "depth": 8}
								if obj[1] == 'ngan':
									# {"feature": "chan", "instances": 15, "metric_value": 2.1736, "depth": 9}
									if obj[2] == 'ngan':
										# {"feature": "chieu cao", "instances": 9, "metric_value": 2.281, "depth": 10}
										if obj[0] == 'thap':
											return 'Ban cung'
										elif obj[0] == 'cao':
											return 'Ban cung'
										else: return 'Ban cung'
									elif obj[2] == 'dai':
										# {"feature": "chieu cao", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[0] == 'cao':
											return 'Ban cung'
										elif obj[0] == 'thap':
											return 'Ban cung'
										else: return 'Ban cung'
									else: return 'Ban cung'
								elif obj[1] == 'dai':
									# {"feature": "chieu cao", "instances": 13, "metric_value": 1.8543, "depth": 9}
									if obj[0] == 'cao':
										# {"feature": "chan", "instances": 7, "metric_value": 1.9502, "depth": 10}
										if obj[2] == 'dai':
											return 'Boi'
										elif obj[2] == 'ngan':
											return 'Ban cung'
										else: return 'Ban cung'
									elif obj[0] == 'thap':
										# {"feature": "chan", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[2] == 'dai':
											return 'Ban cung'
										elif obj[2] == 'ngan':
											return 'Ban cung'
										else: return 'Ban cung'
									else: return 'Ban cung'
								else: return 'Ban cung'
							elif obj[8] == 'kem':
								# {"feature": "chieu cao", "instances": 10, "metric_value": 0.9219, "depth": 8}
								if obj[0] == 'cao':
									# {"feature": "tay", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1] == 'dai':
										# {"feature": "chan", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == 'dai':
											return 'Boi'
										elif obj[2] == 'ngan':
											return 'Dap xe'
										else: return 'Dap xe'
									elif obj[1] == 'ngan':
										return 'Dap xe'
									else: return 'Dap xe'
								elif obj[0] == 'thap':
									# {"feature": "tay", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1] == 'ngan':
										# {"feature": "chan", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == 'ngan':
											return 'Dap xe'
										elif obj[2] == 'dai':
											return 'Dap xe'
										else: return 'Dap xe'
									elif obj[1] == 'dai':
										return 'Dap xe'
									else: return 'Dap xe'
								else: return 'Dap xe'
							else: return 'Dap xe'
						elif obj[3] == 'yeu':
							# {"feature": "chieu cao", "instances": 20, "metric_value": 0.9219, "depth": 7}
							if obj[0] == 'cao':
								# {"feature": "tay", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[1] == 'dai':
									# {"feature": "chan", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[2] == 'dai':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Boi'
										elif obj[8] == 'kem':
											return 'Boi'
										else: return 'Boi'
									elif obj[2] == 'ngan':
										return 'Dap xe'
									else: return 'Dap xe'
								elif obj[1] == 'ngan':
									return 'Dap xe'
								else: return 'Dap xe'
							elif obj[0] == 'thap':
								# {"feature": "tay", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[1] == 'ngan':
									# {"feature": "chan", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[2] == 'ngan':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Dap xe'
										elif obj[8] == 'kem':
											return 'Dap xe'
										else: return 'Dap xe'
									elif obj[2] == 'dai':
										return 'Dap xe'
									else: return 'Dap xe'
								elif obj[1] == 'dai':
									return 'Dap xe'
								else: return 'Dap xe'
							else: return 'Dap xe'
						else: return 'Dap xe'
					elif obj[7] == 'kem':
						return 'Ban cung'
					else: return 'Ban cung'
				else: return 'Dap xe'
			elif obj[4] == 'yeu':
				# {"feature": "chieu cao", "instances": 60, "metric_value": 1.9069, "depth": 4}
				if obj[0] == 'cao':
					# {"feature": "tay", "instances": 36, "metric_value": 1.8366, "depth": 5}
					if obj[1] == 'dai':
						# {"feature": "suc ben", "instances": 28, "metric_value": 1.9502, "depth": 6}
						if obj[7] == 'tot':
							# {"feature": "toc do", "instances": 24, "metric_value": 1.9183, "depth": 7}
							if obj[9] == 'nhanh':
								# {"feature": "can bang", "instances": 18, "metric_value": 1.8366, "depth": 8}
								if obj[8] == 'tot':
									# {"feature": "chan", "instances": 12, "metric_value": 1.9183, "depth": 9}
									if obj[2] == 'dai':
										# {"feature": "than tren", "instances": 7, "metric_value": 1.9502, "depth": 10}
										if obj[3] == 'khoe':
											return 'Boi'
										elif obj[3] == 'yeu':
											return 'Boi'
										else: return 'Boi'
									elif obj[2] == 'ngan':
										# {"feature": "than tren", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[3] == 'khoe':
											return 'Ban cung'
										elif obj[3] == 'yeu':
											return 'Boxing'
										else: return 'Boxing'
									else: return 'Boxing'
								elif obj[8] == 'kem':
									# {"feature": "chan", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[2] == 'dai':
										# {"feature": "than tren", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'khoe':
											return 'Boi'
										elif obj[3] == 'yeu':
											return 'Boi'
										else: return 'Boi'
									elif obj[2] == 'ngan':
										return 'Boxing'
									else: return 'Boxing'
								else: return 'Boxing'
							elif obj[9] == 'cham':
								# {"feature": "chan", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'dai':
									# {"feature": "than tren", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[3] == 'khoe':
										# {"feature": "can bang", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8] == 'tot':
											return 'Boi'
										elif obj[8] == 'kem':
											return 'Boi'
										else: return 'Boi'
									elif obj[3] == 'yeu':
										return 'Boi'
									else: return 'Boi'
								elif obj[2] == 'ngan':
									return 'Ban cung'
								else: return 'Ban cung'
							else: return 'Boi'
						elif obj[7] == 'kem':
							return 'Ban cung'
						else: return 'Ban cung'
					elif obj[1] == 'ngan':
						return 'Ban cung'
					else: return 'Ban cung'
				elif obj[0] == 'thap':
					# {"feature": "than tren", "instances": 24, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'khoe':
						# {"feature": "can bang", "instances": 20, "metric_value": 0.7219, "depth": 6}
						if obj[8] == 'tot':
							# {"feature": "tay", "instances": 18, "metric_value": 0.5033, "depth": 7}
							if obj[1] == 'ngan':
								# {"feature": "chan", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[2] == 'ngan':
									# {"feature": "suc ben", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "toc do", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[9] == 'nhanh':
											return 'Ban cung'
										elif obj[9] == 'cham':
											return 'Ban cung'
										else: return 'Ban cung'
									elif obj[7] == 'kem':
										return 'Ban cung'
									else: return 'Ban cung'
								elif obj[2] == 'dai':
									return 'Ban cung'
								else: return 'Ban cung'
							elif obj[1] == 'dai':
								return 'Ban cung'
							else: return 'Ban cung'
						elif obj[8] == 'kem':
							return 'The duc dung cu'
						else: return 'The duc dung cu'
					elif obj[3] == 'yeu':
						return 'The duc dung cu'
					else: return 'The duc dung cu'
				else: return 'Ban cung'
			else: return 'Ban cung'
		elif obj[5] == 'yeu':
			return 'Ban cung'
		else: return 'Ban cung'
	elif obj[6] == 'kem':
		# {"feature": "toc do", "instances": 96, "metric_value": 1.2516, "depth": 2}
		if obj[9] == 'nhanh':
			# {"feature": "than duoi", "instances": 64, "metric_value": 1.5, "depth": 3}
			if obj[4] == 'khoe':
				# {"feature": "than tren", "instances": 56, "metric_value": 1.3788, "depth": 4}
				if obj[3] == 'khoe':
					# {"feature": "chieu cao", "instances": 36, "metric_value": 1.3921, "depth": 5}
					if obj[0] == 'cao':
						# {"feature": "tay", "instances": 20, "metric_value": 1.5219, "depth": 6}
						if obj[1] == 'dai':
							# {"feature": "chan", "instances": 12, "metric_value": 1.585, "depth": 7}
							if obj[2] == 'dai':
								# {"feature": "tong the", "instances": 6, "metric_value": 1.585, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Boxing'
										elif obj[8] == 'kem':
											return 'Boxing'
										else: return 'Boxing'
									else: return 'Boxing'
								else: return 'Boxing'
							elif obj[2] == 'ngan':
								# {"feature": "tong the", "instances": 6, "metric_value": 1.585, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 6, "metric_value": 1.585, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 6, "metric_value": 1.585, "depth": 10}
										if obj[8] == 'tot':
											return 'Boxing'
										elif obj[8] == 'kem':
											return 'Boxing'
										else: return 'Boxing'
									else: return 'Boxing'
								else: return 'Boxing'
							else: return 'Boxing'
						elif obj[1] == 'ngan':
							# {"feature": "chan", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'dai':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							elif obj[2] == 'ngan':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							else: return 'Cau long'
						else: return 'Cau long'
					elif obj[0] == 'thap':
						# {"feature": "tay", "instances": 16, "metric_value": 1.0, "depth": 6}
						if obj[1] == 'dai':
							# {"feature": "chan", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'dai':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							elif obj[2] == 'ngan':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							else: return 'Cau long'
						elif obj[1] == 'ngan':
							# {"feature": "chan", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'dai':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							elif obj[2] == 'ngan':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Cau long'
										elif obj[8] == 'kem':
											return 'Cau long'
										else: return 'Cau long'
									else: return 'Cau long'
								else: return 'Cau long'
							else: return 'Cau long'
						else: return 'Cau long'
					else: return 'Cau long'
				elif obj[3] == 'yeu':
					# {"feature": "chieu cao", "instances": 20, "metric_value": 0.7219, "depth": 5}
					if obj[0] == 'cao':
						# {"feature": "tay", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[1] == 'dai':
							# {"feature": "chan", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'dai':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Boxing'
										elif obj[8] == 'kem':
											return 'Boxing'
										else: return 'Boxing'
									else: return 'Boxing'
								else: return 'Boxing'
							elif obj[2] == 'ngan':
								# {"feature": "tong the", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'khoe':
									# {"feature": "suc ben", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7] == 'tot':
										# {"feature": "can bang", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8] == 'tot':
											return 'Boxing'
										elif obj[8] == 'kem':
											return 'Boxing'
										else: return 'Boxing'
									else: return 'Boxing'
								else: return 'Boxing'
							else: return 'Boxing'
						elif obj[1] == 'ngan':
							return 'Dap xe'
						else: return 'Dap xe'
					elif obj[0] == 'thap':
						return 'Dap xe'
					else: return 'Dap xe'
				else: return 'Dap xe'
			elif obj[4] == 'yeu':
				return 'Boxing'
			else: return 'Boxing'
		elif obj[9] == 'cham':
			return 'Dap xe'
		else: return 'Dap xe'
	else: return 'Dap xe'
