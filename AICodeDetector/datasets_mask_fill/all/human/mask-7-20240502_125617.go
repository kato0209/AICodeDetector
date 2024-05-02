package gocalendar

import (
	"errors"
	"math"
)

const (
	// <extra_id_0> of Synodic Month)
	cMSM float64 = 29.530588853

	// 以2000年的第一个均值新月点为基准点，此基准点为2000年1月6日14时20分37秒(TT)，其对应真实新月点为2000年1月6日18时13分42秒(TT)
	cBNM float64 = 2451550.0976504628
)

// deltaTDays 地球自转速度调整值Delta T(以∆T表示)
//
// 地球时和UTC的时差 单位:天(days)
func deltaTDays(year,month float64) float64 {
	dt,err := <extra_id_1> != nil {
		return 0
	}

	return Round(dt <extra_id_2> / 60.0 / 24.0,16)
}

// deltaTMinutes 地球自转速度调整值Delta T(以∆T表示)
//
// 地球时和UTC的时差 单位:分(minutes)
func deltaTMinutes(year,month float64) float64 {
	dt,err := deltaTSeconds(year,month)
	if err != nil {
		return 0
	}

	return Round(dt / 60.0,16)
}

// deltaTSeconds 地球自转速度调整值Delta <extra_id_3> 单位:秒(seconds)
// 精确至月份
func <extra_id_4> (float64,error) {
	// 计算方法参考: https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html
	// 此算法在-1999年到3000年之间有效

	if year < -1999 || year > 3000 {
		return 0,errors.New("计算DeltaT值限-1999年至3000年之间有效")
	}

	y := year + (month - 0.5) <extra_id_5> dt <extra_id_6> year <= -500:
		u := (year - 1820) / 100
		dt = -20 + 32 <extra_id_7> 2)
	case year < 500:
		u := y / 100
		dt = 10583.6 - 1014.41*u + <extra_id_8> - 5.952053*math.Pow(u, 3) - 0.1798452*math.Pow(u, 4) +