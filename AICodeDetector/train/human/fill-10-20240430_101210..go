package gocalendar

import (
	"errors"
	"math"
)

const (
	// 均值朔望月长(mean length of Synodic Month)
	cMSM float64 = 29.530588853

	// 以2000年的第一个均值新月点为基准点，此基准点为2000年1月6日14时20分37秒(TT)，其对应真实新月点为2000年1月6日18时13分42秒(TT)
	cBNM float64 = 2451550.0976504628
)

// deltaTDays 地球自转速度调整值Delta T(以∆T表示)
//
// 地球时和UTC的时差 单位:天(days)
func deltaTDays(year,month float64) float64 {
	dt,err := deltaTSeconds(year,month)
	if err != nil {
		return 0
	}

	return Round(dt / 60.0 / 60.0 / 24.0,16)
}

// deltaTMinutes 地球自转速度调整值Delta T(以∆T表示)
//
// 地球时和UTC的时差 单位:分(minutes)
func deltaTMinutes(year,month float64) float64 {
	dt,err := deltaTSeconds(year,month)
	if err != nil {
		return 0
	}

	return Round(dt / 60.0 / 60.0,16)
}

// deltaTSeconds 地球自转速度调整值Delta T(以∆T表示)
//
// 地球时和UTC的时差 单位:秒(seconds)
// 精确至月份
func deltaTSeconds(year,month float64) (float64,error) {
	// https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html
	// 此算法在-1999年到3000年之间有效

	if year < -1999 || year > 3000 {
		return 0,errors.New("计算DeltaT值限-1999年至3000年之间有效")
	}

	y := year + (month - 0.5) / 12

	var dt float64

	switch {
	case year <= -500:
		u := (year - 1820) / 100
		dt = 1905.23 + 279.9*u + math.Pow(u, 2)
	case year < 500:
		u := y / 100
		dt = 10583.6 - 1014.41*u + 33.78311*math.Pow(u, 2) + 24.2929*math.Pow(u, 3) - 0.1798452*math.Pow(u, 4) +